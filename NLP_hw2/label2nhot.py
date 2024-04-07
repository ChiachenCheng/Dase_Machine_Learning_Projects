if __name__=='__main__':
    labeltext = open('label.txt', 'r', encoding='utf-8')
    f = open('nhots.txt', 'w', encoding='utf-8')
    dict = {}
    labels = []
    summary = {}
    for i in labeltext:
        labelstr = str(i).replace("[",'').replace("]\n",'').replace("'", '')
        label = labelstr.split(', ')
        # if label == [""] :
        #     continue
        # print(label)
        labels.append(label)
        for j in label:
            if j not in dict:
                dict[j] = len(dict)
                summary[j] = 1
            else:
                summary[j] += 1

    # print(dict)
    print(len(dict))
    print(len(labels))
    temp = sorted(summary.items(), reverse=1, key=lambda s:s[1])
    # print(temp)

    lable_maxn = 30
    partlabels = {}
    i = 0
    for label in temp:
        if i >= lable_maxn:
            break
        partlabels[label[0]] = i
        i += 1

    print(partlabels)
    nhots = []
    for label in labels:
        nhot = [0 for x in range(len(partlabels))]
        for eachlabel in label:
            if eachlabel in partlabels:
                nhot[partlabels[eachlabel]] = 1
        nhots.append(nhot)
        f.write(str(nhot)+ '\n')

    for i in range(6):
        print(labels[i*10000])
        print(nhots[i*10000])
