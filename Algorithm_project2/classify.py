from pyhanlp import *

def load_content_data():
    input = open('content1w.txt', 'r', encoding='utf-8')
    text = []
    for eachline in input:
        text.append(eachline)
    return text

if __name__ == '__main__':
    text = load_content_data()
    keywords = []
    dict = {}
    k = 20
    for i in range(len(text)):
        document = text[i]
        keyword = HanLP.extractKeyword(document, k)
        for word in keyword:
            if word not in dict.keys():
                dict[word] = []
            dict[word].append(i)
        keywords.append(keyword)
        if i % 200 == 0:
            print(i)
            print(keyword)

    dict = sorted(dict.items(),key=lambda x:len(x[1]),reverse=True)
    print(dict)

    for i in range(10):
        entry = dict[i]
        output = open('content'+entry[0]+'.txt', 'w', encoding='utf-8')
        for j in entry[1]:
            output.write(text[j])
        output.close()

