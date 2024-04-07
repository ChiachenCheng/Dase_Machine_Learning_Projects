from stanfordcorenlp import StanfordCoreNLP

def load_data():
    input = open('sentences.txt', 'r', encoding='utf-8')
    text = []
    for eachline in input:
        text.append(eachline)
    return text

if __name__ == '__main__':
    output = open('standependence.txt', 'w', encoding='utf-8')
    nlp = StanfordCoreNLP(r'/Users/mac/opt/anaconda3/lib/python3.8/site-packages/stanford-corenlp-4.1.0', lang='zh')
    text = load_data()
    for eachline in text:
        # 分詞
        result = nlp.word_tokenize(eachline)
        print(result)
        print(result, file=output)

        # 詞性標註
        result = nlp.pos_tag(eachline)
        # print(result)
        print(result, file=output)

        # 命名實體識別
        result = nlp.ner(eachline)
        # print(result)
        print(result, file=output)

        # 句法成分分析
        result = nlp.parse(eachline)
        # print(result)
        print(result, file=output)

        # 依存句法分析
        result = nlp.dependency_parse(eachline)
        # print(result)
        print(result, file=output)

        print('\n', file=output)