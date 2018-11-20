# -*- coding: utf-8 -*-
# step3：train_word2vec_model.py 用于训练模型
'''script parameters：
C:\work\experiment\word2vec\zhwiki\corpus\wiki.zh.text.seg C:\work\experiment\word2vec\zhwiki\word2vec_model\wiki.zh.text.model
C:\work\experiment\word2vec\zhwiki\word2vec_model\wiki.zh.text.vector
'''
import logging
import os.path
import sys
import multiprocessing
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__=='__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]   #argv[0]默认是系统参数，自定义参数从argv[1]开始

    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(outp1)   #   输出文件默认为ANSI编码
    # model.save_word2vec_format(outp2, binary=False)   #会报错DeprecationWarning: Deprecated. Use model.wv.save_word2vec_format instead.
    model.wv.save_word2vec_format(outp2, binary=False)  #   输出文件默认为utf-8编码