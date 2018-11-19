# -*- coding: utf-8 -*-
# step2：jiebaCut.py 用于分词

import os
import sys
import jieba
import logging
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)

logging.basicConfig(format='%(asctime)s: %(levelname)s:  %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))

read_from_file = "corpus/zhwiki.text"
write_to_file = 'corpus/wiki.zh.seg.txt'
with open(read_from_file, 'r', encoding='utf-8') as file:
    i = 0
    for line in file:   #为防止内存爆炸，采用按行读入处理方式
        seg = jieba.cut(line.strip(), cut_all=False)
        output = '/'.join(seg)
        output = output + '\n'
        with open(write_to_file, 'a+', encoding='utf-8') as s:
            s.write(output)
        i = i + 1
        if (i % 10000 == 0):  # 以万为单位输出INFO信息
            logger.info("Saved " + str(i) + " articles")
    file.close()
    logger.info("Finished Saved " + str(i) + " articles")

#   读取单行文本
with open(write_to_file, 'r', encoding='utf-8') as ff:
    lines = ff.readlines()  #读取所有行
    print('分词文件' + write_to_file + '第一行为：' + lines[0])
    print('反词文件' + write_to_file + '最后一行为：' + lines[-1])
    ff.close()
