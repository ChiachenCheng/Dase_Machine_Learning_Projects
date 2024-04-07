from gensim.models import FastText
import os
# sentences = [["你", "是", "谁"], ["我", "是", "中国人"]]

def myfunction(sz,win,mc):
    sentences=[]
    f = open('reduce_zhiwiki.txt', 'r',encoding='utf-8')
    result = list()
    for line in f.readlines():
        line = line.strip()
        line=line.split(' ')
        sentences.append(line)
        # print(line)

    model = FastText(sentences,  size=sz, window=win, min_count=mc, iter=10,min_n = 3 , max_n = 6, word_ngrams = 0)
    # print(model['你'])  # 词向量获得的方式
    # print(model.wv['你']) # 词向量获得的方式
    st = './test2/' + str(sz) + '_' + str(win) + '_' + str(mc) + '_'
    model.save(st + 'fasttext.model')
    model.wv.save_word2vec_format(st + 'fasttext_wordembedding.txt', binary=False)
    print(st + " finish\n")

if __name__ == '__main__':

    myfunction(64, 41, 3)
    myfunction(128, 51, 3)
    myfunction(96, 51, 3)
    myfunction(64, 51, 3)

    # os.system('say "your program has finished"')