#Frequency频率统计
import nltk
from nltk import FreqDist

#做个词库
corpus = 'this is my sentence. this is my life. this is the day.'
tokens = nltk.word_tokenize(corpus)
print('tokens: ', tokens)

#借助NLTK的FreqDist统计词频
fdist = FreqDist(tokens)
print(fdist['is']) #看看is在整篇文章中出现的次数


#现在，我们把最常用的50个单词拿出来
standard_freq_vector = fdist.most_common(50)
size = len(standard_freq_vector)
print(standard_freq_vector)
print('size = ', size)


#Func: 按照出现频率大小，记录下每一个单词的位置
def position_lookup(v):
    res = {}
    counter = 0
    for word in v:
        res[word[0]] = counter
        counter += 1
    return res


#把标准的单词位置记录下来
standard_position_dict = position_lookup(standard_freq_vector)
print('位置对照表：\n',standard_position_dict)


#这时，如果有一个新句子：
sentence = 'this is cool'
freq_vector = [0] * size #新建一个和我们标准vector同样大小的向量
tokens = nltk.word_tokenize(sentence)
for word in tokens:
    try: #如果在我们的词库里出现过，就在‘标准位置’上+1
        freq_vector[standard_position_dict[word]] += 1
    except KeyError: #如果是新词，pass
        continue
print('------新句子的向量表示：------\n')
print(sentence, '\n',freq_vector)

#第二个句子
sentence2 = 'he is her husband, and this is legal.'
sent_vector = [0] * size
token2 = nltk.word_tokenize(sentence2)
for word in token2:
    try:
        sent_vector[standard_position_dict[word]] += 1
    except KeyError:
        continue
print(sentence2, '\n', sent_vector)