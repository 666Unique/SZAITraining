import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split ###

df = pd.read_csv('CSVComments.csv')
# 73划分训练集和测试集
train_df,test_df = train_test_split(df,test_size=0.3,random_state=42) 
# 打印训练集
print('训练集: \n',train_df)
# 打印测试集
print('测试集: \n',test_df)
# 打印训练集的数量
print('训练集数量:',len(train_df))
# 打印训练集中三条文本内容
print('训练集部分文本:',train_df[:3])


