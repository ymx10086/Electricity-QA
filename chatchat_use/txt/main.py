import json

def read_for_ans(question : str) -> str:
    """
    Read the answer for the question from the json file
    """
    with open('./que_ans.json', 'r') as f:
        data = json.load(f)["que_ans"]
    filename = ""
    for i in data:
        if i["question"] == question:
            filename = i["answer"]
    if filename == "":
        return ""
    else:
        with open('./llm/' + filename, 'r') as f:
            ans = f.read()
        return ans
    
if __name__ == "__main__":
    print(read_for_ans("请介绍一下如何使用src-oepkgs构建工程完成软件包上传"))