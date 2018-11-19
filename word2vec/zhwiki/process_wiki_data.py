# -*- coding: utf-8 -*-
# step1：process_wiki_data.py 用于解析XML，将XML的wiki数据转换为text格式

import logging
import sys
import os.path
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.corpora import WikiCorpus

if __name__=='__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s:  %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp = sys.argv[1:3]   #argv[0]默认是系统参数，自定义参数从argv[1]开始
    space = ""
    i = 0

    output = open(outp, 'w', encoding='utf-8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):    #以万为单位输出INFO信息
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
