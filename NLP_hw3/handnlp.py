from pyhanlp import *

def load_data():
    input = open('sentences.txt', 'r', encoding='utf-8')
    text = []
    for eachline in input:
        text.append(eachline)
    return text

def load_content_data():
    input = open('content100.txt', 'r', encoding='utf-8')
    text = []
    for eachline in input:
        text.append(eachline)
    return text

def feature_content(document):
    # 关键词提取
    keyword = HanLP.extractKeyword(document, 2)
    # print(keyword)
    print(keyword, file=outputcontent)

    # 自动摘要
    summary = HanLP.extractSummary(document, 3)
    print(summary)
    print(summary, file=outputcontent)

def feature(document):
    # 依存句法分析
    try:
        depend = HanLP.parseDependency(document)
        # print(depend)
        print(depend, file=output)
    except:
        return

if __name__ == '__main__':
    output = open('handdependence.txt', 'w', encoding='utf-8')
    outputcontent = open('handkeycontent.txt', 'w', encoding='utf-8')

    text = load_data()
    for eachline in text:
        print(HanLP.segment(eachline))
        feature(eachline)
        print('\n', file=output)

    contents = load_content_data()
    for eachline in contents:
        feature_content(eachline)
        print('\n', file=outputcontent)
