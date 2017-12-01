# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:52:19 2017

@author: shen
"""
import numpy as np
from keras.models import Sequential												 #import Sequential(DNN很好擴充的基礎模型)
from keras.layers.core import Dense,Activation									 #import core(基本層)
from keras.optimizers import  Adam												 #import Optimizers
from keras.datasets import mnist												 #import dataset
from keras.utils import np_utils                                                 #為後續轉換成One-hot encoding
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']
# define class labels
labels = [1,1,1,1,1,0,0,0,0,0]
# integer encode the documents - 每個字都有一個座號
vocab_size = 50
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)

# to have the same length vector - 每個向量維度歸一化
## The sequences have different lengths and Keras prefers inputs to be vectorized and all inputs to have the same length.
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)

