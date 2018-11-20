word2vec训练中文模型：https://www.zybuluo.com/hanxiaoyang/note/472184


word2vec训练过程记录：（所有的语料和中间生成文件均未上传，如有需要请email：jaquanC@126.com）
1、中文维基百科原始语料文件zhwiki-latest-pages-articles.xml.bz2是XML文档，使用process_wiki_data.py脚本将其转换为text文件格式。
2、使用jiebaCut.py脚本对文件zhwiki.text进行分词，得到分词文件wiki.zh.text.seg和wiki.zh.seg.txt。这里自己纯属瞎玩，运行了两次脚本，生成了两个不同文本格式的分词文件，其实只用其中一个文件即可。
3、使用train_word2vec_model.py脚本训练模型，分词文件之一作为输入，输出的是两个文件：word2vec_model/wiki.text.model和word2vec_model/wiki.zh.text.vector
4、测试模型效果
5、后续改进：http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C/comment-page-1

