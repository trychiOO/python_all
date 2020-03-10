# -*- coding: utf-8 -*-
import jieba
import codecs
import jieba.posseg as pseg

# 建立3个dict 存放   姓名  关系  和每lines 出现人名的关系

names = {}
relationships = {}
lineNames = []
"""
#----------------读取  并切词----------------#
#读入《釜山行》剧本的每一行，对其做分词（判断该词的词性是不是“人名”[词性编码：nr]，
# 如果该词的词性不为nr，则认为该词不是人名），
# 提取该行（段）中出现的人物集，存入lineName中。
# 之后对出现的人物，更新他们在names中的出现次数。
"""
jieba.load_userdict("dict.txt")

with codecs.open("busan.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])
        # print(lineNames[-1])
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue
            lineNames[-1].append(w.word)  # 把 切词放到
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = 0
                print(type(names))
            names[w.word] += 1
for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] == 1
            else:
                relationships[name1][name2] =relationships[name1][name2] +1

with codecs.open("busan_note.txt" ,"w" ,"utf8") as f:
    f.write("Id lebel   Wigth")

    for name , times in n
