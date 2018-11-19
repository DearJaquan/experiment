# -*- coding: utf-8 -*-
# step2：jiebaCut.py 用于分词

import jieba

with open("corpus/zhwiki.text", 'r', encoding='utf-8') as file:
    for line in file:   #为防止内存爆炸，采用按行读入处理方式
        seg = jieba.cut(line.strip(), cut_all=False)
        output = '/'.join(seg)
        output = output + '\n'
        with open('corpus/wiki.zh.text.seg', 'a+', encoding='utf-8') as s:
            s.write(output)
    file.close()