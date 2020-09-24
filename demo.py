# -*-coding:utf-8-*-
import pandas as pd
import jieba
import copy
import numpy as np
import re

'''
原文文档：
C:/Users/陈乙鑫/Desktop/orig.txt
对比文档：
C:/Users/陈乙鑫/Desktop/orig_0.8_add.txt
C:/Users/陈乙鑫/Desktop/orig_0.8_del.txt
C:/Users/陈乙鑫/Desktop/orig_0.8_dis_1.txt
C:/Users/陈乙鑫/Desktop/orig_0.8_dis_10.txt
C:/Users/陈乙鑫/Desktop/orig_0.8_dis_15.txt

'''
# 原文文档分词
URL1 = str()
URL1 = input('请输入样本文档路径')
book_a0 = open(URL1, 'r', encoding='utf-8')
book_a1 = book_a0.read()
book_a0.close()
book_a = re.sub(r'[^\u4e00-\u9fa5]', "", book_a1)  # 只保留中文
book_a_lcut = jieba.lcut(book_a)
print('该文本有', len(book_a_lcut), '个字')

print('***********************************************************')
print('这是原文', book_a1)
print('***********************************************************')
print('去除代码部分', book_a)

# 对比文档分词

URL2 = str()
URL2 = input('请输入对比文档路径')
book_b0 = open(URL2, 'r', encoding='utf-8')
book_b1 = book_b0.read()
book_b0.close()
book_b = re.sub(r'[^\u4e00-\u9fa5]', "", book_b1)  # 只保留中文
book_b_lcut = jieba.lcut(book_b)

print('该文本有', len(book_b_lcut), '个字')

print('***********************************************************')
print('这是对比文', book_b1)
print('***********************************************************')
print('去除代码部分', book_b)

# 构建一个全集
same0 = list(book_b_lcut)

for word in book_a_lcut:
    if word not in book_b_lcut:
        same0.append(word)

arr1 = []
arr2 = []
same = list(set(same0))
same1 = list(set(same))
print('重复合集')
print(same0)
print('***********************************************************')
print('非重复合集')
print(same)
print('***********************************************************')
print('重复合集长度')
print(len(same0))
print('***********************************************************')
print('非重复合集长度')
print(len(same))

# 停词处理
stop_0 = open('/Users/陈乙鑫/Desktop/stop_word.txt', 'r', encoding='utf-8')
stop_1 = stop_0.read()
stop_0.close()
stop = re.sub(r'[^\u4e00-\u9fa5]', "", stop_1)  # 只保留中文
stop_lcut = jieba.lcut(stop)

for x in same:
    if x in stop_lcut:
        same1.remove(x)
print('***********************************************************')
print('***************************************************')
print('stop_lcut', stop_lcut)
print('***********************************************************')

# 构建词频向量
# 1
for word1 in same1:
    arr1.append(book_a_lcut.count(word1))
print('arr1', arr1)

print('***********************************************************')

# 2
for word2 in same1:
    arr2.append(book_b_lcut.count(word2))
print('arr2', arr2)

# 计算余弦

sum = 0
sq1 = 0
sq2 = 0
for cnt in range(len(same1)):
    sum += arr1[cnt] * arr2[cnt]
    sq1 += pow(arr1[cnt], 2)
    sq2 += pow(arr2[cnt], 2)

cos = sum / ((sq1 * sq2) ** 0.5)
print(cos)












