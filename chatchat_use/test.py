import gradio as gr
import os
import shutil
from chains.local_doc_qa import *
from configs.model_config import *
import nltk
import json


nltk.data.path = [os.path.join(os.path.dirname(__file__), "nltk_data")] + nltk.data.path

# return top-k text chunk from vector store
VECTOR_SEARCH_TOP_K = 6

# LLM input history length
LLM_HISTORY_LEN = 2

FLAG = 0

def get_vs_list():
    if not os.path.exists(VS_ROOT_PATH):
        return []
    return os.listdir(VS_ROOT_PATH)


vs_list = ["新建知识库"] + get_vs_list()

embedding_model_dict_list = list(embedding_model_dict.keys())

llm_model_dict_list = list(llm_model_dict.keys())

def init_model():
    try:
        reply = """模型已成功加载，可以开始对话，或从右侧选择模式后开始对话"""
        print(reply)
        return reply
    except Exception as e:
        print(e)
        reply = """模型未成功加载，请到页面左上角"模型配置"选项卡中重新选择后点击"加载模型"按钮"""
        if str(e) == "Unknown platform: darwin":
            print("该报错可能因为您使用的是 macOS 操作系统，需先下载模型至本地后执行 Web UI，具体方法请参考项目 README 中本地部署方法及常见问题："
                  " https://github.com/imClumsyPanda/langchain-ChatGLM")
        else:
            print(reply)
        return reply
    
model_status = init_model()

vs_path = "./vector_store/abc"

def langchain_ans(query):

    # print(vs_path)
    related_docs = get_knowledge_based_answer(query=query, vs_path=vs_path, chat_history=[], streaming=False) 
    
    # print(related_docs)
    
    content = "\n".join([doc.page_content for doc in related_docs])


    return content
    

if __name__ == "__main__":
    query = "在地震设防烈度为7度及以上的电气设施安装设计中，设备引线和设备间连线宜采用（），其长度应留有余量。当采用硬母线时，应有（）或伸缩接头过渡。？"
    
    print(langchain_ans(query))
    