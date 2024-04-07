from ltp import LTP

ltp = LTP()
input = open('content中国.txt', 'r', encoding='utf-8')
sentences = open('sentences中国.txt', 'w', encoding='utf-8')
text = []
for eachline in input:
    sents = ltp.sent_split([eachline])
    for sent in sents:
        if sent[len(sent) - 1] == '.':
            sentences.write(sent)
        else:
            sentences.write(sent + '\n')
    sentences.write('\n')