# -*- coding: utf-8 -*-
from gensim.models import FastText

def myfunction(sz,win,mc):
    sentences=[]
    f = open('words.txt', 'r',encoding='utf-8')
    result = list()
    for line in f.readlines():
        line = line.strip()
        line=line.split(' ')
        sentences.append(line)
        # print(line)

    model = FastText(sentences,  size=sz, window=win, min_count=mc, iter=10, min_n = 1 , max_n = 20, word_ngrams = 0)
    st = ''
    model.save(st + 'fasttext.model')
    model.wv.save_word2vec_format(st + 'fasttext_wordembedding.txt', binary=False)
    print(st + " finish\n")

if __name__ == '__main__':
    myfunction(32, 7, 1)