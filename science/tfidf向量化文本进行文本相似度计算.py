# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:17:07 2022

@author: Administrator
"""

#TfidfVectorizer是sklearn中的库，可以用来计算TF-IDF值,计算文档中的每一个词语的tf-idf值。形成多篇文档的tf-idf向量化矩阵
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import jieba
import os
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
# 对文本句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.lcut(sentence.strip())
    stopwords = stopwordslist("C:\\Users\\86175\\Desktop\\第2讲文本特征抽取与表示\\data1\\stopword.txt")  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords: #判断这个词是否在停用词列表中  是的话删除 不要了 不是的话  保留
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
def cos_sim(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    cos = np.dot(a,b)/(a_norm * b_norm)
    return cos
path = "C:\\Users\\86175\\Desktop\\第2讲文本特征抽取与表示\\data" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
txts = []
for file in files: #遍历文件夹
    position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
    print (position)           
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        data = f.read()   #读取文件
        txts.append(data)
txts1=txts#将依次读入的每一个txt，单独作为列表的一个元素
output=[]#定义一个空列表用于存储分词和去除停用词后的结果    分词结果是一个list of str类型
jieba.load_userdict("C:\\Users\\86175\\Desktop\\第2讲文本特征抽取与表示\\data1\\usedict.txt")  # 载入自定义词典,需要注意txt文档要utf—8编码，文件路径字符串形式
for i in txts1:
    line_seg = seg_sentence(str(i))
    output.append(line_seg)# 分词后的结果存储在列表output中了
corpus=output

vectorizer = TfidfVectorizer(min_df=5)#取每一篇文档频次大于5的词语特征项
X = vectorizer.fit_transform(corpus)#fit_transform方法将语料转化成TF-IDF权重矩阵
wordname=vectorizer.get_feature_names()#，get_feature_names方法可得到词汇表

numpy1=X.toarray()#m行n列处值的含义是词汇表中第n个词在第m篇文档的TF-IDF值。
df1=pd.DataFrame(numpy1)#转换成datafram类型
df1.columns=wordname#修改datafram列名称

#索引出前两篇的文献
df0=list(df1.iloc[0])
df11=list(df1.iloc[1])

#把词袋模型表示的文本，转换成向量的形式
t1  = np.array(df0)
t2  = np.array(df11)
#运用余弦夹角计算两篇文档之间的相似度
tfidfcos2=cos_sim(t1,t2)
print(tfidfcos2)
