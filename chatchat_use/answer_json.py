import json
import os
import sys
import pandas as pd
import numpy as np
from chatuse import *
import random
import sys
import time
import os



# 控制台输出记录到文件
class Logger(object):
    def __init__(self, file_name="Default.log", stream=sys.stdout):
        self.terminal = stream
        self.log = open(file_name, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

if __name__ == "__main__":
    
    # 自定义目录存放日志文件
    log_path = './Logs_/'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # 日志文件名按照程序运行时间设置
    log_file_name = log_path + 'log-' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.log'
    # 记录正常的 print 信息
    sys.stdout = Logger(log_file_name)
    # 记录 traceback 异常信息
    sys.stderr = Logger(log_file_name)
    # 读取question.json文件
    
    with open('question.json', 'r') as f:
        questions = json.load(f)
    # print(questions)
    # answers = [{"answer" : "亚马逊"}]
    answers = []
    for item in questions:
        id = item['id']
        question = item['question']
        type = item['type']
        tmp_answer = {}
        dict =  {"A" : 0, "B" : 0, "C" : 0, "D" : 0}
        if type == "单选":
            
            dict["A"]  = 0
            dict["B"]  = 0
            dict["C"]  = 0
            dict["D"]  = 0
            answer_A = item['A']
            answer_B = item['B']
            answer_C = item['C']
            answer_D = item['D']
            options = [answer_A, answer_B, answer_C, answer_D]
            
            answer = run_chatglm2(question, options)
            answer1 = run_chatglm2(question, options)
            answer2 = run_chatglm2(question, options)

            # 选取出现次数最多的答案作为最终答案
            dict[answer] += 1
            dict[answer1] += 1
            dict[answer2] += 1

            answer = max(dict, key=dict.get)
            
            print("dict", dict)
            tmp_answer = {'ID': id, 'answer': answer}
            
        elif type == "多选":
            answer_A = item['A']
            answer_B = item['B']
            answer_C = item['C']
            answer_D = item['D']
            options = [answer_A, answer_B, answer_C, answer_D]
            answer1 = run_chatglm_multiple(question, options)
            answer2 = run_chatglm_multiple(question, options)
            answer = []
            # 判定a，b，c，d选项是否在answer1，answer2，answer3，answer4中出现，如果出现则加入answer
            if "A" in answer1 and "A" in answer2:
                answer.append('A')
            if "B" in answer1 and "B" in answer2 :
                answer.append('B')
            if "C" in answer1 and "C" in answer2:
                answer.append('C')
            if "D" in answer1 and "D" in answer2:
                answer.append('D')
            answer = "、".join(answer)
            if answer == "":
                # 如果answer为空，则随机选"A"，"B"，"C"，"D"中的一个
                answer = random.choice(['A', 'B', 'C', 'D'])
            tmp_answer = {'ID': id, 'answer': answer}
                
        elif type == "问答":
            answer1 = run_chatglm_answer(question)
            answer2 = run_chatglm_answer(question, fine=True)
            answer3 = run_chatglm_answer(question)
            tmp_answer = {'ID': id, 'answer': answer1 + answer2 + answer3}
        print(tmp_answer)
        answers.append(tmp_answer)
        with open('GPT_answer_join.json', 'a+', encoding="utf-8") as f:
            # 将答案写入json文件，追加写入
            print("写入文件")
            json.dump(tmp_answer, f, ensure_ascii = False)
            f.write(',\n')
        
    # 将答案写入json文件
    with open('GPT_answer.json', 'w', encoding="utf-8") as f:
        json.dump(answers, f, ensure_ascii = False)

        
        
        