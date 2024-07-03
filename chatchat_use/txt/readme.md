## 自动化构建问题对

为了方便扩展和md问题对生成，特编写此文档和md_read.py脚本

#### 构建好的问题对实例

```
{
    "que_ans": [
        {
            "id": 0,
            "question": "example question",
            "answer": "id_0.txt"
        }
    ],
    "count": 0
}
```

#### 构建方法

首先需要进入到相关路径

```
cd oec-application/tools/oepkgs-talk-robot/txt
```

通过运行md_read.py，将文档添加到内容中，要求文档标题和内容之间的关系鲜明，例如现有`rpm.md`文档需要构建，则需要运行

```
python md_read.py --input rpm.md
```

进而完成问题对的扩展