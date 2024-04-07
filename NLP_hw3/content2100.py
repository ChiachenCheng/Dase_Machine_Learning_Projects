# -*- coding: utf-8 -*-
import re

def my_function():
    i = 0
    input_file = open('content.txt', 'r', encoding='utf-8')
    f = open('content100.txt', 'w', encoding='utf-8')
    max_sentence = 100

    for text in input_file:
        text = text.replace("######","")
        if(text == "\n"):
            continue
        text = re.sub(r"\n+", '\n', text)
        text = text.replace(" ", "")
        if len(text) < 50:
            continue
        f.write(text)
        i = i + 1
        if i >= max_sentence:
            break
    f.close()

if __name__ == '__main__':
    my_function()