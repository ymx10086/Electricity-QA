import markdown_it
import json
import argparse

# 读取Markdown文件并解析为HTML
def read_and_parse_markdown(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    md = markdown_it.MarkdownIt()
    parsed_html = md.render(markdown_text)

    return parsed_html

# 处理问题的HTML标签和空格和数字和标点符号
def process_question(question):
    question = question.replace("<h1>", "")
    question = question.replace("</h1>", "")
    question = question.replace("<h2>", "")
    question = question.replace("</h2>", "")
    question = question.replace("<h3>", "")
    question = question.replace("</h3>", "")
    question = question.replace("<h4>", "")
    question = question.replace("</h4>", "")
    question = question.replace("<h5>", "")
    question = question.replace("</h5>", "")
    question = question.replace("<h6>", "")
    question = question.replace("</h6>", "")
    # 数字和标点符号都去掉
    question = ''.join([i for i in question if not i.isdigit() and i not in '!"#$%&\'()*+,/:;?@.[\\]^_`{|}~'])
    # 去掉空格
    question = question.replace(" ", "")
    return question
    

# 根据HTML解析的结果，提取问题和答案
def extract_questions_and_answers(html):
    questions = []
    answers = []
    
    in_question = False
    current_question = ""
    current_answer = ""
    
    lines = html.split("\n")
    
    print(lines)

    for line in lines:
        if line.strip().startswith("<h"):
            if in_question:
                answers.append(current_answer)
                current_answer = ""
                in_question = False
            current_question = line.strip()
            in_question = True
            questions.append(process_question(current_question))
        else:
            current_answer += line.strip() + "\n"

    answers.append(current_answer)
    
    return questions, answers

# 保存问题和答案为JSON文件
def save_as_json(questions, answers, output_filename):
    with open(output_filename, 'r', encoding='gbk') as json_file:
        data = json.load(json_file)

    que_ans = data["que_ans"]
    id_final = que_ans[-1]["id"] + 1

    for i in range(len(questions)):
        filename = "id_" + str(id_final + i) + ".txt"
        que_ans.append({"id": id_final + i, "question": questions[i], "answer": filename})
        with open("./llm/" + filename, "w", encoding="gbk") as f:
            f.write(answers[i])

    data["que_ans"] = que_ans
    data["count"] = len(que_ans)
    
    with open(output_filename, 'w', encoding='gbk') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    # input_filename = "北向开源软件包适配迁移详细指导.md"  # 替换为你的Markdown文件路径

    parser = argparse.ArgumentParser()

    parser.add_argument('--input', type=str, default='北向开源软件包适配迁移详细指导.md', help='input markdown file')
    output_filename = "output.json"  # 保存为JSON的文件名

    args = parser.parse_args()
    input_filename = args.input
    
    parsed_html = read_and_parse_markdown(input_filename)
    print(parsed_html)
    questions, answers = extract_questions_and_answers(parsed_html)
    # save_as_json(questions, answers, output_filename)

    cur_que_ans_json = "que_ans.json"
    save_as_json(questions, answers, cur_que_ans_json)
