import torch.cuda
import torch.backends
import os

embedding_model_dict = {
    "ernie-tiny": "nghuyong/ernie-3.0-nano-zh",
    "ernie-base": "nghuyong/ernie-3.0-base-zh",
    "text2vec-base": "shibing624/text2vec-base-chinese",
    "text2vec": "./text2vec-large-chinese",
}

# Embedding model name
EMBEDDING_MODEL = "text2vec"

# Embedding running device
EMBEDDING_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# supported LLM models
llm_model_dict = {
    "chatyuan": "ClueAI/ChatYuan-large-v2",
    "chatglm-6b-int4-qe": "THUDM/chatglm-6b-int4-qe",
    "chatglm-6b-int4": "THUDM/chatglm-6b-int4",
    "chatglm-6b-int8": "THUDM/chatglm-6b-int8",
    "chatglm2-6b": "./chatglm2",
}

# LLM model name
LLM_MODEL = "chatglm2-6b"

# Use p-tuning-v2 PrefixEncoder
USE_PTUNING_V2 = False

# LLM running device
LLM_DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

VS_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vector_store", "")

UPLOAD_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content", "")

# 基于上下文的prompt模版，请务必保留"{question}"和"{context}"
PROMPT_TEMPLATE = """已知信息为【水泵类负载在工况点1、2 运行时，对应的扬程和转速分别为 H1、H2和 N1、N2,它的扬程（H）与转速（N）符合H2/H1 = (N2/N1)^2关系式。】请回答问题：{question}

    注意你的回答应该按照以下要求： 
    1.你回答的格式应该是: 我认为上面的说法是xx的。 
    2.你只需要回答问题相关内容，“不要回答无关的内容”。 
    3.你不需要进行计算。
    4.你的回答只能“来源于提供的资料”。
"""

# 匹配后单段上下文长度
CHUNK_SIZE = 500
