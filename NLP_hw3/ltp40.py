#!/usr/bin/env python
# coding=utf-8
from ltp import LTP

def load_content_data():
    input = open('content100.txt', 'r', encoding='utf-8')
    text = []
    for eachline in input:
        text.append(eachline)
    return text

def load_data():
    input = open('sentences.txt', 'r', encoding='utf-8')
    text = []
    for eachline in input:
        text.append(eachline)
    return text

if __name__ == '__main__':
    ltp = LTP()
    text = load_data()
    # 分句
    sents = ltp.sent_split(text)
    output = open('ltpdependence.txt', 'w', encoding='utf-8')
    sentences = open('sentences.txt', 'w', encoding='utf-8')

    for sent in sents:
        if sent[len(sent)-1] == '.':
            sentences.write(sent)
        else:
            sentences.write(sent + '\n')

    sentences.close()
    text = load_data()

    for sent in text:
        # 分词
        seg, hidden = ltp.seg([sent])
        print(seg)
        print(seg, file=output)

        # 词性标注
        pos = ltp.pos(hidden)
        # print(pos)
        print(pos, file=output)

        # 依存句法分析
        dep = ltp.dep(hidden)
        # print(dep)
        print(dep, file=output)

        # 语义依存分析（树）
        sdptree = ltp.sdp(hidden, graph=False)
        # 语义依存分析（图）
        sdpgraph = ltp.sdp(hidden, graph=False)
        # print(sdptree)
        # print(sdpgraph)
        print(sdptree, file=output)
        print(sdpgraph, file=output)

        print('\n', file=output)