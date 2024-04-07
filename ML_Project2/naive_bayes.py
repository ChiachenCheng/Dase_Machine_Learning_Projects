from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import KFold
import numpy as np

def naive_bayes(X, Y, train_index, test_index):
    print("TRAIN:", train_index, "TEST:", test_index)
    x_train, x_test = X[train_index], X[test_index]
    y_train, y_test = Y[train_index], Y[test_index]
    # x_train,x_test,y_train,y_test = train_test_split(news_data.data,news_data.target,test_size=0.2)
    #3.进行特征抽取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)
    #4.进行朴素贝叶斯算法分类
    bayes = MultinomialNB(alpha=1.0)
    bayes.fit(x_train,y_train)
    y_predict = bayes.predict(x_test)
    print("测试集的预测结果为：",y_predict)
    score = bayes.score(x_test,y_test)
    print("模型的预测准确率为：",score)
    return score

if __name__ == '__main__':
    # 1.读取数据
    news_data = fetch_20newsgroups(subset="all")
    X = np.array(news_data.data)
    Y = np.array(news_data.target)
    # 2.划分训练集，测试集
    kf = KFold(n_splits=5)
    kf.get_n_splits(X)
    scores = []
    for train_index, test_index in kf.split(X):
        scores.append(naive_bayes(X, Y, train_index, test_index))
    print("最终的预测准确率为：", np.array(scores).mean())