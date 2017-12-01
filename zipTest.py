# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:42:34 2017
Parsing document!!
@author: shen
"""

input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
def find_bigrams(input_list):
  return zip(input_list, input_list[1:], input_list[2:])

list = []

for i in find_bigrams(input_list):
    list.append(i)
    