# -*- coding: utf-8 -*-
import jieba
import re

def my_function():
    space = ' '
    i = 0
    l = []
    input_file = open('content.txt', 'r', encoding='utf-8')
    f = open('words.txt', 'w', encoding='utf-8')
    length = []

    for text in input_file:
        text = text.replace("######","")
        if(text == "\n"):
            continue
        #text = re.sub(r"[\s+\!\/_,$%^*()?;；:-【】+\"\']+|[+——！-，;:：。？、~@#￥%……&*（）]+", " ", text)
        text = re.sub(r"\n+", '\n', text)
        text = text.replace(" ", "")
        #print(text)
        seg_list = list(jieba.cut(text))  # 分词
        for temp_term in seg_list:
            l.append(temp_term)
        length.append(len(l))
        if l != None:
            f.write(space.join(l) + '\n')
        l = []
        i = i + 1

        if (i % 2000 == 0):
            print('Saved ' + str(i) + ' articles')
    f.close()

    print(i)
    s = 0
    min = 10000000000
    max = 0
    for j in length:
        s += j
        if (j == 0):
            i -= 1
        if(j < min and j != 0):
            min = j
        if(j > max):
            max = j
    print(s/i)
    print(max)
    print(min)
    print(length.sort())



if __name__ == '__main__':
    my_function()