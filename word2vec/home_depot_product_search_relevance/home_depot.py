import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer

df_train = pd.read_csv('train.csv', encoding='ISO-8859-1')
df_test = pd.read_csv('test.csv', encoding='ISO-8859-1')
df_desc = pd.read_csv('product_descriptions.csv', encoding='ISO-8859-1')

# df_train.head()
# df_test.head()
# df_desc.head()

# 合并测试/训练集，便于统一做文本预处理
df_all = pd.concat((df_train, df_test), axis=0, ignore_index=True)
df_all = pd.merge(df_all, df_desc, how='left', on='product_uid')
print('预处理前df_all的样子： \n')
print(df_all.head())
print(df_all.shape)

'''文本预处理过程'''
stemmer = SnowballStemmer('english')

def str_stemmer(s):
    return " ".join([stemmer.stem(word) for word in s.lower().split()])

# 简单统计关键词的出现次数
def str_common_word(str1, str2):
    return sum(int(str2.find(word) >= 0) for word in str1.split())

df_all['search_term'] = df_all['search_term'].map(lambda x:str_stemmer(x))
df_all['product_title'] = df_all['product_title'].map(lambda x:str_stemmer(x))
df_all['product_description'] = df_all['product_description'].map(lambda x:str_stemmer(x))
print('经过预处理后，df_all的样子：\n')
print(df_all.head())


'''提取文本特征'''

# 关键词的长度
df_all['len_of_query'] = df_all['search_term'].map(lambda x:len(x.split())).astype(np.int64)
df_all.head()

# 标题中有多少关键词重合
df_all['commons_in_title'] = df_all.apply(lambda x:str_common_word(x['search_term'],x['product_title']), axis=1)

# 描述中有多少关键词重合
df_all['commons_in_desc'] = df_all.apply(lambda x:str_common_word(x['search_term'], x['product_description']), axis=1)

# 我们将不能被机器学习模型处理的column给drop掉
df_all = df_all.drop(['search_term', 'product_title', 'product_description'], axis=1)

# 分开训练和测试集
print('df_train.index = ',df_train.index)
df_train = df_all.loc[df_train.index]
print('df_test.index = ', df_test.index)
df_test = df_all.loc[df_test.index]

# 记录下测试集的id，上传结果时可以对得上号
test_ids = df_test['id']

# 分离出y_train
y_train = df_train['relevance'].values

# 把原集合中的label删去，否则就是cheating了
X_train = df_train.drop(['id', 'relevance'], axis=1).values
X_test = df_test.drop(['id', 'relevance'], axis=1).values


'''建立模型'''
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor
from sklearn.model_selection import cross_val_score

# 用CV结果保证公正客观性，调试不同的alpha值
params = [1,3,5,7,8,9,10]
test_scores = []
for param in params:
    print('随机森林的深度：', param)
    clf = RandomForestRegressor(n_estimators=30, max_depth=param)
    test_score = np.sqrt(-cross_val_score(clf, X_train, y_train, cv=5, scoring='neg_mean_squared_error'))
    print('经过5轮交叉验证后的test_score = ', test_score)
    test_scores.append(np.mean(test_score))


# 画图显示效果
import matplotlib.pyplot as plt
plt.plot(params, test_scores)
plt.title("Param vs CV Error")
plt.savefig("C:\\work\\SougouLab\\word2vec\\home_depot_product_search_relevance\\paramVScv_error.png")
plt.show()

# 我们测试出的最优解建立模型，并跑一下测试集
rf = RandomForestRegressor(n_estimators=30, max_depth=6)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
# 将结果放进PD，做成CSV上传
pd.DataFrame({"id": test_ids, "relevance": y_pred}).to_csv("submission.csv", index=False)
