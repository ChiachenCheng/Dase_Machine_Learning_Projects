# coding=utf-8
import pandas as pd
from gensim.models import FastText


def my_function():
    model = FastText.load('fasttext.model')
    print(model.similarity('白宫', '五角大楼'))
    print(model.similarity('君士坦丁堡', '伊斯坦布尔'))

    result = pd.Series(model.most_similar(u'特朗普'))  # 查找近义相关词
    print(result)
    result1 = pd.Series(model.most_similar(u'新冠'))
    print(result1)
    print(model.wv['中国'])  # 查看中国的词向量（单个词语的词向量）


if __name__ == '__main__':
    my_function()