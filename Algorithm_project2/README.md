# Text summarization

#### 姓名：郑佳辰        学号：10182100359

##### README.md

本文件，项目文件说明文档。

##### classify.py

对所有商业新闻进行简单分类。输入文件为content1w.txt，输出到生成的content中国.txt等10个文件。从输出文件中挑选出一个文件进行文本摘要的生成。

##### getsentence.py

对content中国.txt进行分句，也可简单修改后对其他类别文本进行分句。输入文件为content中国.txt，输出到生成的sentence中国.txt文件中。

##### summary.py

进行文本摘要生成。输入文件为sentence中国.txt或对应格式的其他类别文件。生成的多篇摘要连同关键词等信息输出到控制台中。在实验报告中有对应实验结果截图。

##### content1w.txt

初始时的商业新闻语料，有5000多条，作为classify.py的输入。

##### content中国.txt

中国对应类的商业新闻语料。运行classify.py后生成，作为getdentence.py的输入。

##### sentences中国.txt

中国对应类的商业新闻语料分句后的结果。每行为一句话，不同篇之间用空行分隔。运行getdentence.py后生成，作为summary.py的输入用于生成摘要。

##### text summarization.pdf

PDF版本的实验报告。

##### text summarization.docx

word版本的实验报告。