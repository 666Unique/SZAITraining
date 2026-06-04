import pandas as pd
import numpy as np
#打印相关函数用于查找
print(dir(pd),dir(np),dir(pd.DataFrame))
data_1 = {
    '评论ID': np.arange(1,21),
    '评论者': ['用户'+str(i) for i in range(1,21)],
    '评分': np.random.randint(1,6,size=20),
    '电影评论':[
        '特别好','不错','特别好','很不错','特别好',
        '一般','特别一般','很一般','还行','就那样',
        '差','很差','特别差','差得不行','非常差',
        '看不下去','真不想看','烂片','非常烂','看不下去',
    ],
    '评论时间': pd.date_range('2024-01-01',periods=20,freq='D')
}
# 创建DataFrame
df_1 = pd.DataFrame(data_1) #
# # 保存到csv中
# df_1.to_csv("CSVComments.csv",index = False)
# # 如需要从csv中读取
# data = pd.read_csv('CSVComments.csv')
# # 打印前10行
# print(f'从CSV中读出的数据为:\n {data.head(10)}') #

# 打印前10行
print(f'前10行数据为:\n {df_1.head(10)}') ##
# 打印某一列
print(f'打印的列为:\n {df_1['评论ID']}') ##
# 筛选评分大于3的列
print(f'评分筛选后:\n {df_1[df_1['评分']>=3]}') ## Pandas的条件过滤Boolean Indexing允许通过返回Boolean index的Series来筛选数据
# 删除重复的评论
df_filetered = df_1.drop_duplicates(subset=['电影评论']) ## 只保留首次出现的数据
print(f'去重后:\n {df_filetered}') 

#格式转换(比如时间)
Time_Data = {
    '评论时间':[
        '2024/01/01',
        '2024.01.02',
        '2024年01月03日'
    ]
}
#创建DataFrame
df_time = pd.DataFrame(Time_Data)
#清洗函数
def clean_time_str(s):
    s=s.replace("年","-").replace("月","-").replace("日","")
    s=s.replace("/","-").replace(".","-")
    return s.strip()
df_time['清洗后'] = df_time['评论时间'].apply(clean_time_str)
df_time['标准格式'] = pd.to_datetime(df_time['清洗后'],errors = 'coerce').dt.strftime('%Y-%m-%d') ##将日期格式化为'年月日'字符串
print(df_time)