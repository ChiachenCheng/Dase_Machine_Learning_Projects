from ltp import LTP
from pyhanlp import *
import random
import numpy as np

def summary(passage):
    k = 10
    ltp = LTP()
    document = ''
    sentences = []
    for eachtext in passage:
        for eachline in eachtext:
            document = document + eachline
            sentences.append(eachline)
    keywords = HanLP.extractKeyword(document, k)
    summary_test = HanLP.extractSummary(document, 10)
    print(keywords)
    non_list = [0 for i in range(k)]
    appear = []
    sents = []
    for sentence in sentences:
        appear_line = []
        seg, hidden = ltp.seg([sentence])
        for keyword in keywords:
            if keyword in seg[0]:
                appear_line.append(1)
            else:
                appear_line.append(0)
        if appear_line != non_list:
            appear.append(appear_line)
            sents.append(sentence)

    cover = [0 for i in range(k)]
    delta_si = [-1 for i in range(len(sentences))]
    summarynum = []
    maxi = 0
    while True:
        for i in range(len(appear)):
            if delta_si[i] == 0:
                continue
            s = 0
            for j in range(k):
                if (cover[j] == 0) and (appear[i][j] == 1):
                    s += 1
            delta_si[i] = s
            if delta_si[i] > delta_si[maxi]:
                maxi = i
        if delta_si[maxi] == 0:
            break
        summarynum.append(maxi)
        for j in range(k):
            if appear[maxi][j] == 1:
                cover[j] = 1

    summarynum.sort()
    print(summarynum)
    summary = ''
    for i in summarynum:
        summary = summary + sents[i]
    print(summary)
    summary_rate.append(len(summarynum)/len(sentences))
    print(summary_test)
    print('\n')

def choose_passage(texts):
    k = 10
    ran = [i for i in range(len(texts))]
    random.shuffle(ran)
    passage = []
    for i in range(k):
        passage.append(texts[ran[i]])
    return passage

def load_data():
    input = open('sentences中国.txt', 'r', encoding='utf-8')
    texts = []
    text = []
    for eachline in input:
        if eachline == '\n':
            texts.append(text)
            text = []
        else:
            eachline = eachline[:-1]
            text.append(eachline)
    return texts

if __name__ == "__main__":
    N = 10
    summary_rate = []
    texts = load_data()
    for i in range(N):
        passage = choose_passage(texts)
        summary(passage)
    print(summary_rate)
    print(np.array(summary_rate).mean())