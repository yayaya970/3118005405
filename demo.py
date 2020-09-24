# -*-coding:utf-8-*-


import jieba
import re
def main():

    # 原文文档：C:/Users/陈乙鑫/Desktop/orig.txt
    # 对比文档：

    # 原文文档分词
    # URL1=str()
    # URL1=input('请输入样本文档路径')
# URL1=sys.argv[1]
    book_a0 = open('C:/Users/陈乙鑫/Desktop/orig.txt', 'r', encoding='utf-8')
    book_a1 = book_a0.read()
    book_a0.close()
    book_a = re.sub(r'[^\u4e00-\u9fa5]', "", book_a1)  # 只保留中文
    book_a_lcut = jieba.lcut(book_a)
    print('该文本有', len(book_a_lcut), '个字')

    # 对比文档分词

    # URL2=str()
    # URL2=input('请输入样本文档路径')
    # URL2=sys.argv[2]
    book_b0 = open('C:/Users/陈乙鑫/Desktop/orig_0.8_add.txt', 'r',
               encoding='utf-8')
    book_b1 = book_b0.read()
    book_b0.close()
    book_b = re.sub(r'[^\u4e00-\u9fa5]', "", book_b1)  # 只保留中文
    book_b_lcut = jieba.lcut(book_b)
    print('该文本有', len(book_b_lcut), '个字')

    # print('去除代码部分',book_b_lcut)


    # 构建一个全集
    same0 = list(book_b_lcut)

    for word in book_a_lcut:
        if word not in book_b_lcut:
            same0.append(word)

    arr1 = []
    arr2 = []
    same1 = list(set(same0))
    same = list(same1)

    book_s0 = open('C:/Users/陈乙鑫/Desktop/stop_word.txt', 'r',
               encoding='utf-8')
    book_s1 = book_s0.read()
    book_s0.close()
    book_s_lcut = book_s1.split('\n')

    # same0是重复的全集，same1是不重复的全集；same是停词之后的全集
    for stop in same1:
        if stop in book_s_lcut:
            same.remove(stop)

    # 构建词频向量
    # 1
    for word1 in same:
        arr1.append(book_a_lcut.count(word1))
    '''print('arr1')
    print(arr1)'''

    # print('***********************************************************')

    # 2
    for word2 in same:
        arr2.append(book_b_lcut.count(word2))
    '''print('arr2')
    print(arr2)'''

    # 计算余弦

    sum = 0
    sq1 = 0
    sq2 = 0
    for cnt in range(len(same)):
        sum += arr1[cnt] * arr2[cnt]
        sq1 += pow(arr1[cnt], 2)
        sq2 += pow(arr2[cnt], 2)

    # 结果只取小数点后两位

    cos = sum / ((sq1 * sq2) ** 0.5)

    cos = round(cos, 2)
    cos = str(cos)
    print(cos)

    file_handle = open('C:/Users/陈乙鑫/Desktop/result.txt', mode='w')
    # file_handle=open(sys.argv[3],mode='w')
    file_handle.truncate()
    file_handle.write(cos)
    file_handle.close()

if __name__ == "__main__":
    main()
