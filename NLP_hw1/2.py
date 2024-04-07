# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function(s,sz,win,mc):
    wiki_news = open('reduce_zhiwiki.txt', 'r',encoding='utf-8')
    model = Word2Vec(LineSentence(wiki_news), sg=s, size=sz, window=win, min_count=mc, workers=6)
    #                                      训练算法 词向量大小   窗口大小    最小词频      线程数
    st = './test1/' + str(s) + '_' + str(sz) + '_' + str(win) + '_' + str(mc) + '_'
    model.save(st + 'zhiwiki_news.word2vec')
    model.wv.save_word2vec_format(st +'word2vec_format.txt')

if __name__ == '__main__':
    my_function(0, 128, 91, 7)
    my_function(0, 128, 91, 3)

    # my_function(0, 150, 27, 5)
    # my_function(0, 150, 29, 5)

    # os.system('say "程序运行完毕"')