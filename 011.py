
import pandas as pd
from sklearn.model_selection import train_test_split
url = "https://cdn.tzspace.cn/exam/20240519-level3-exam/exam4/rich_texts.csv"
df = pd.read_csv(url)

#任务一
# 随机打乱并分为训练集和测试集，比例为7:3
train_df, test_df = train_test_split(df, test_size=0.3, random_state=42) 

# 填充<2><3>处，打印训练集和测试集
print("训练集：")
print(train_df)
print("\n测试集：")
print(test_df)
#任务一结束

#任务二
# 打印训练集的数量
print(f"训练集数量: {len(train_df)}")
# 打印训练集中的部分文本内容
print("训练集中三条文本内容：")
print(train_df.head(3)) 
#任务二结束