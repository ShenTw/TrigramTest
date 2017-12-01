# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:47:27 2017

@author: shen
"""
import numpy as np

from keras.models import Sequential												 #import Sequential(DNN很好擴充的基礎模型)
from keras.layers.embeddings import Embedding
# Bigrams
class Trigrams:       
    def __init__(self):
        self.weighted = False
        self.documents = {}
        self.corpus_dict = {}
        self.Trigrams = []
    def find_Trigrams(self,input_list):
        return zip(input_list, input_list[1:], input_list[2:])
      