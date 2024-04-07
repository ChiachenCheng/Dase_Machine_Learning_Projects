# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import time
import random
import warnings
import numpy as np
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.core import Dense, Activation, Dropout
from gensim.models import FastText
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
warnings.filterwarnings("ignore")

def load_data(len1):
    words1 = open('words.txt', 'r',encoding='utf-8')
    model = FastText.load('fasttext.model')
    nhots = open('nhots.txt', 'r', encoding='utf-8')
    labels_maxn = 30
    words_maxn = 32
    words = []
    for eachline in words1:
        if eachline != '\n' and eachline != ' \n':
            line = eachline.replace('\n','').replace('\t','')
            line = re.sub(r" +", ' ', line)
            list1 = line.split(' ')
            i = 0
            for wd in list1:
                if (wd == '') or (wd == '\n') or (wd == '\xa0'):
                    del list1[i]
                i += 1
            if (list1 != []) and (list1 != None):
                words.append(list1)
    dict_vec={}
    for word in model.wv.index2word:
        dict_vec[word] = list(model.wv[word])

    x_train=[]
    y_train=[]
    maxn = 700
    for nhotstr in nhots:
        nhotstr = nhotstr.replace("[", '').replace(']\n', '')
        list2 = nhotstr.split(', ')
        y_train_one = [int(n) for n in list2]
        y_train.append(y_train_one)

    zerolist = [0 for i in range(labels_maxn)]
    for i in range(len1):
        if y_train[i] == zerolist:
            continue
        embedding_one=[]
        words_one=words[i]
        len_word = len(words_one)
        if len_word >= maxn:
            words_one = words_one[0:maxn]
            for j in range(maxn):
                if words_one[j] in dict_vec:
                    embedding_one.append(dict_vec[words_one[j]])
                else:
                    dict_vec[words_one[j]]=[random.gauss(0,10) for temp in range(words_maxn)]
                    embedding_one.append(dict_vec[words_one[j]])
        else:
            for k in range(maxn-len_word):
                words_one.append("#")
            for j in range(maxn):
                if words_one[j] in dict_vec:
                    embedding_one.append(dict_vec[words_one[j]])
                else:
                    dict_vec[words_one[j]] = [random.gauss(0,10) for temp in range(words_maxn)]
                    embedding_one.append(dict_vec[words_one[j]])
        x_train.append(embedding_one)

    y_train_suc = []
    for y_train_one in y_train:
        if y_train_one == zerolist:
            continue
        y_train_suc.append(y_train_one)
    y_train = y_train_suc

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    return x_train,  y_train

if __name__=='__main__':
    start = time.time()

    x_train, y_train=load_data(60156)#20条训练数据
    print(np.array(x_train).shape,flush=True)
    print(np.array(y_train).shape,flush=True)
    # 有效数据54242个

    model = Sequential()
    model.add(LSTM(input_dim=32, output_dim=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(output_dim=30))
    model.add(Activation("sigmoid"))
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.fit(x_train, y_train, batch_size=128, nb_epoch=10, validation_split=0.2)
    print(model.summary(),flush=True)

    #进行测试并得到精度
    predicted = model.predict(x_train)
    predicted=predicted.tolist()
    predicted_last=[]
    for i in range(len(predicted)):
        predicted_last+=predicted[i]
    for i in range(len(predicted_last)):
        if predicted_last[i]>0.5:
            predicted_last[i]=1
        else:
            predicted_last[i]=0
    y_train=y_train.tolist()
    y_train_last=[]
    for i in range(len(y_train)):
        y_train_last += y_train[i]

    acc=0
    truepositive = 0
    truenegative = 0
    falsepositive = 0
    falsenegative = 0
    for i in range(len(y_train_last)):
        if predicted_last[i]==y_train_last[i]:
            acc+=1
            if predicted_last[i]==1:
                truepositive += 1
            else:
                truenegative += 1
        else:
            if predicted_last[i]==1:
                falsepositive += 1
            else:
                falsenegative += 1
    print(truepositive,truenegative,falsepositive,falsenegative)
    print('all accuracy:')
    print(acc / len(y_train_last))
    print('1 precision:')
    print(truepositive / (truepositive + falsepositive))
    print('0 precision:')
    print(truenegative / (truenegative + falsenegative))
    print('1 recall:')
    print(truepositive / (truepositive + falsenegative))
    print('0 recall:')
    print(truenegative / (truenegative + falsepositive))
