from transformers import AutoTokenizer, AutoModel, AutoConfig
import os
import platform
import regex as re
import random
from test import langchain_ans
import requests
import time
import difflib
import torch
luo = False
cnt_ = 0

# 原推理模型
tokenizer = AutoTokenizer.from_pretrained("./chatglm2", trust_remote_code=True)
# model = AutoModel.from_pretrained("./chatglm2", trust_remote_code=True).to("cuda:0")



# 多显卡支持，使用下面两行代替上面一行，将num_gpus改为你实际的显卡数量
from utils import load_model_on_gpus
model = load_model_on_gpus("./chatglm2", num_gpus=8)

# 微调模型
config = AutoConfig.from_pretrained("./chatglm2", trust_remote_code=True)
# tokenizer = AutoTokenizer.from_pretrained("/home/master/zhoujian/Documents/llm/chatglm2", trust_remote_code=True)
config.pre_seq_len = 128
# config.prefix_projection = model_args.prefix_projection
ptuning_checkpoint = "./chatglm2/czx/ChatGLM2-6B/ptuning/output/final-answer/checkpoint-10000"
print(f"Loading prefix_encoder weight from {ptuning_checkpoint}")
fine_model = AutoModel.from_pretrained("./chatglm2", config=config, trust_remote_code=True)
prefix_state_dict = torch.load(os.path.join(ptuning_checkpoint, "pytorch_model.bin"))
new_prefix_state_dict = {}
for k, v in prefix_state_dict.items():
    if k.startswith("transformer.prefix_encoder."):
        new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
fine_model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)
quantization_bit = 4
print(f"Quantized to {quantization_bit} bit")
fine_model = fine_model.quantize(quantization_bit)
fine_model = fine_model.to("cuda:0").eval()

model = model.eval()

def process(response, question, tag = True):
    # 去掉response中的换行符
    response = response.replace("\n", "")
    # 将response用句号分割成多个句子
    response = response.split("。")
    # print(response)
    
    # 与问题相似度最高的两个句子
    max_index = 0
    max_score = 0
    second_index = 0
    second_score = 0
    for i in range(len(response)):
        score = similarity(response[i], question)
        if score > max_score:
            second_index = max_index
            second_score = max_score
            max_index = i
            max_score = score
        elif score > second_score:
            second_index = i
            second_score = score
    
    # print("max_score:", max_score)
            
    # print("max_index:", max_index)
    # print("second_index:", second_index)
    # 将与问题相似度最高的两个句子拼接起
    response = response[max_index] + "。" + response[second_index]
    
    if max_score < 0.5 and tag:
        response_, _ = fine_model.chat(tokenizer, question, history=[])
        torch.cuda.empty_cache()
        response = response_[:1000] + "。" + response
            
    return response
    

def similarity(text1, text2):
    headers = {     'Connection': 'close' }
    param = {"text1" : text1, "text2" : text2}
    
    
    
    # try:
    #     response = requests.get("https://api.pearktrue.cn/api/textdifference/", params=param, headers=headers)
    # except Exception as e:
    #     time.sleep(1)
    #     return similarity(text1, text2)
    # # r.encoding = 'utf-8'
    # # print(response.json())
    
    # resp = response.json()
    # if resp["code"] == 200:
    #     score =  resp["data"]["similarity"]
    # else:
    #     return 0
    
    # # score 1.00% 字符串转换成float类型
    # score = float(score[:-1])
    
    score = difflib.SequenceMatcher(None, text1, text2).quick_ratio()
    score = float("%.2f" % score)
    
    return score

def build_prompt(question, options):
    
    prompt_f = '''
    注意你的回答应该按照以下要求： 
    1.你回答的格式应该是: 我认为上面的说法是xx的。 
    2.你只需要回答问题相关内容，不要回答无关的内容。 
    3.你不需要进行计算。
    4.你的回答只能来源于提供的资料。
    '''
    # prompt += ""
    prompts = []
    for i in range(len(options)):
        # 正则匹配其中的括号内容，将括号内容替换成选项，要求替换的（）中间可能有空格，但是不能有其他字符
        que = re.sub(r"（\s*）", options[i], question)

        tmp =  que + "这个说法是否正确呢？\n" + prompt_f

        prompts.append(tmp)
        

    
    return prompts

def lang_build_prompt_single(question, options, response, fine = False):
    prompt_s = "已知信息如下:\n"
    prompt_f = '''
    注意你的回答应该按照以下要求： 
    1.你回答的格式应该是: 我认为上面的说法是xx的，因为xxx。
    2.需要完全依据已知信息进行回答问题。 
    3.你不需要进行计算，但可以进行简单的单位换算，例如25%等于0.25。
    4.回答尽量简洁清晰，不要重复。
    '''
    # prompt += ""
    prompts = []
    for i in range(len(options)):
        # 正则匹配其中的括号内容，将括号内容替换成选项，要求替换的（）中间可能有空格，但是不能有其他字符
        try:
            # que = re.sub(r"（\s*）", options[i], question)
            que = re.sub(r"（\s*）", "【" + options[i] + "】", question)
        except Exception as e:
            que = question + "括号中填" + options[i]
        # print(que)
        # print("单选题", response)
        # response = "水泵类负载在工况点1、2 运行时，对应的扬程和转速分别为 H1、H2和 N1、N2,它的扬程（H）与转速（N）符合H2/H1 = (N2/N1)^2关系式。"
        tmp = prompt_s + response[:1000] + '\n\n现在你是电力相关领域的专家，请[首先]重复上面的已知信息，[然后]完全严格依据已知信息分析原因[最后]给出回答，可以进行简单的单位换算，如25%等于0.25，不能自行推断，尤其注意【】中的内容，回答问题如下：' + que + "这个说法是正确还是错误呢？\n"
        # print("\n问题信息：",tmp)
        prompts.append(tmp)
        
    # print("问题信息：", prompts)
    
    return prompts

def lang_build_prompt_multiple(question, options, fine = False):
        
    prompt_s = "已知信息如下:\n"
    prompt_f = '''
    注意你的回答应该按照以下要求： 
    1.你需要先重复一遍已知信息。 
    2.你只需要回答问题相关内容，不要回答无关的内容。 
    3.你不需要进行计算。
    4.尽可能严谨，不确定则回答无法确定。
    '''
    # prompt += ""
    prompts = []
    for i in range(len(options)):
        # 正则匹配其中的括号内容，将括号内容替换成选项，要求替换的（）中间可能有空格，但是不能有其他字符
        try:
            que = re.sub(r"（\s*）", "【" + options[i] + "】", question)
            # que = re.sub(r"（\s*）", options[i], question)
        except Exception as e:
            que = question + "括号中填" + options[i]
        # print("que:", que)
        response = langchain_ans(que)
        response = process(response, que)
        # print(que)
        # print("多选题", response)
        # response = "水泵类负载在工况点1、2 运行时，对应的扬程和转速分别为 H1、H2和 N1、N2,它的扬程（H）与转速（N）符合H2/H1 = (N2/N1)^2关系式"
        tmp = prompt_s + response[:1000] + '\n\n现在你是电力相关领域的专家，请完全依据上面的已知信息，可以进行简单的单位换算，如25%等于0.25，不要随意推断，尽量严谨，尤其注意【】中的内容，回答问题如下：' + que + "这个说法和已知信息相同是否正确呢？。\n"
        # print("\n问题信息：",tmp)
        prompts.append(tmp)
        
    # print("问题信息：", prompts)
    
    return prompts

def lang_build_prompt_answer(question, fine = False):
        
    prompt_s = "已知信息为"
    prompt_f = '''
    注意你的回答应该按照以下要求： 
    1.你的回答可以参考提供的资料。
    2.你回答得内容需要尽可能详细。
    3.你回答要尽可能完整，长度尽可能长。
    4.你的回答可以依据常识，但不要太离谱。
    5.回答尽量简洁清晰，不要重复。
    '''
    # prompt += ""
    prompts = []
    response = langchain_ans(question)
    response = response[:1000]
    # print(que)
    # print("问答:", response)
    # response = "水泵类负载在工况点1、2 运行时，对应的扬程和转速分别为 H1、H2和 N1、N2,它的扬程（H）与转速（N）符合H2/H1 = (N2/N1)^2关系式"
    tmp = prompt_s + response + '\n\n现在你是电力相关领域的专家，请尽可能【详细完整全面】地回答下面的问题：\n' + question + "\n"
    # print("\n问题信息：",tmp)
    prompts.append(tmp)
    
    return prompts
    
def run_chatglm2(question, options, fine = False):
    global cnt_
    key = ['A', 'B', 'C', 'D']
    if cnt_ > 2:
        cnt_ = 0
        # return key[random.choice([0, 1, 2, 3])]
        return "C"
    
    if luo:
        querys = build_prompt(question, options)
    else:
        
        response = langchain_ans(question)
        
        if cnt_ < 1:
            response = process(response, question)
            response = response[:1000]
        else:
            response = process(response, question, tag = False)
            
        
        
        querys = lang_build_prompt_single(question, options, response)
    
    # if cnt_ > 0:
    #     for i in querys:
    #         i += "Take a deep breath and work on this problem step-by-step"
   
    
    print("问题：", question)
    print("选项：", options)
    
    waitlist = []
    
    for i in range(len(querys)):
        query = querys[i]
        print(query)
        if fine:

            response, _ = fine_model.chat(tokenizer, query, history=[]) 
                
        else:
            response, _ = model.chat(tokenizer, query, history=[])
            
        print("response:", response)

        if "错误" in response:
            continue
        if "不正确" in response:
            continue
        if "无法确定" in response:             
            continue
        if "不能确定" in response:                          
            continue
        if "正确" in response:
            waitlist.append(i)
    
    if len(waitlist) == 0:
        print("第", cnt_, "次没有推理出正确答案")
        cnt_ += 1
        return run_chatglm2(question, options)
        # return -1
    
    if len(waitlist) == 1:
        print("推理出的正确答案为：", options[waitlist[0]])
        cnt_ = 0
        return key[waitlist[0]]
    
    else:
        # 对waitlist中的数字进行倒序排序
        # waitlist.sort(reverse=True)
        for i in waitlist:
            query = querys[i]
            # print("query:", query)
            response, _ = fine_model.chat(tokenizer, query, history=[]) 
            torch.cuda.empty_cache()
            if "错误" in response:
                continue
            if "不正确" in response:
                continue
            if "正确" in response:
                print("推理出的正确答案为：", options[i])
                cnt_ = 0
                return key[i]
        rst = key[random.choice(waitlist)]
        print("最有可能的答案为：", rst)
        # 随机返回waitlist中的一个元素对应的key
        return rst
    
def run_chatglm_multiple(question, options, fine = False):
    
    if luo:
        querys = build_prompt(question, options)
    else:
        # response = langchain_ans(question)
        # response = process(response, question)
        # response = "露天或半露天的变电所，不应设置在附近有棉、粮及其他易燃、易爆品集中的露天堆场、易暴露在雨雪中的场所"
        querys = lang_build_prompt_multiple(question, options)
    
    key = ['A', 'B', 'C', 'D']
    
    print("问题：", question)
    print("选项：", options)
    
    waitlist = []
    
    for i in range(len(querys)):
        query = querys[i]
        # print("query:", query)
        if fine:
            response, _ = fine_model.chat(tokenizer, query, history=[])
            torch.cuda.empty_cache()
        else:
            response, _ = model.chat(tokenizer, query, history=[])
            torch.cuda.empty_cache()
        # print("response:", response)
        if "错误" in response:
            continue
        if "不正确" in response:
            continue
        if "正确" in response:
            waitlist.append(i)
    
    if len(waitlist) == 0:
        print("没有推理出正确答案")
        
        return "C"
        # return -1
        
    # 对waitlist中的数字进行排序
    waitlist.sort()
        
    keylist = []
    for i in waitlist:
        keylist.append(key[i])
    print("推理出的正确答案为：", keylist)
    
    # 将keylist中的元素转换成字符串
    keylist = "、".join(keylist)
    # print(keylist)
    
    return keylist

def run_chatglm_answer(question, fine = False):
    
    question = lang_build_prompt_answer(question)

    if fine:
        response, _ = fine_model.chat(tokenizer, question, history=[])
        torch.cuda.empty_cache()
    else:
        print(question)
        response, _ = model.chat(tokenizer, question, history=[])
        torch.cuda.empty_cache()

    return response
        
if __name__ == "__main__":
    question = "当高压及低压配电设备设在同一室内时，且二者有一侧顶端有裸露的母线，二者之间的净距不应小于（）。"
    options = ["3m", "2.5m", "2m", "1.5m"]
    answer = run_chatglm_multiple(question, options)
    # score = similarity("水泵类负载在工况点1、2 运行时，对应的扬程和转速分别为 H1、H2和 N1、N2,它的扬程（H）与转速（N）符合H2/H1 = (N2/N1)^2关系式。", "水泵类负载在工况点1、2 运行时，对应的扬程和转速分别为 H1、H2和 N1、N2,它的扬程（H）与转速（N）符合H2/H1 = (N2/N1)^2关系式。")
    # answer = run_chatglm_multiple(question, options)
    
    print(answer)
    