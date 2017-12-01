# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:47:27 2017

@author: shen
"""
import numpy as np

from keras.models import Sequential												 #import Sequential(DNN很好擴充的基礎模型)
from keras.layers.embeddings import Embedding
def find_Trigrams(input_list):
    return zip(input_list, input_list[1:], input_list[2:])

LIST = []
path = "D:/2017Study/Classes/IR/hw5/"
with open(path+'doc_list.txt','r' ) as L:
        
    for line0 in L: # open each document
        line0 = line0.strip('\n')
        path = "D:/2017Study/Classes/IR/hw5/Document/"
        file = path+line0
        # open each document
        with open(file,'r') as f:
            
            listOfWords=[]
            temp= []
            #每篇doc的初始化
            
            for line in f.readlines() : # read the document  #data=f.readline()
                line=line.strip('\n')
                line=line.strip('-1')
                temp = temp + line.split() #temp為該doc的字典(只有字)
                #print("doc : \n" ,line0, "temp : ", temp)
            for i in range(5,len(temp),+1): #扣除前三行不需要的資訊(經切割後為五項)
                listOfWords.append(temp[i])  #listOfwords為該doc的全文字串(分割到 list中)_
                #print("Doc: ", line0, "words",listOfWords)
                
            for each in find_Trigrams(listOfWords): #存成一個documents 文件集 {doc:{字:字數}}
                LIST.append(each)
            
            #length = len(result)
            #總文件數量
      #          numpy.array([for word in result])
            
