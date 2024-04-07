import json
from gensim.models import FastText

stat = {}
word = {}
for i in range(20):
    stat[i] = 0
    word[i] = 0

sentences = []
with open('20news.json','r') as f:
    for l in f:
        data = json.loads(l)
        stat[data["label"]] += 1
        word[data["label"]] += len(data["text"])
        sentences.append(data["text"])

allwords = 0
allnews = 0
for i in range(20):
    allwords += word[i]
    allnews += stat[i]
    word[i] /= stat[i]
print(stat)
print(word)
print(allwords/allnews)

model = FastText(sentences,  size=32, window=7, min_count=1, iter=10, min_n = 1 , max_n = 20, word_ngrams = 0)
st = ''
model.save(st + 'fasttext.model')
model.wv.save_word2vec_format(st + 'fasttext_wordembedding.txt', binary=False)
print(st + " finish\n")



