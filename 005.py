# #任务一
# import pandas as pd
# import numpy as np
# # 创建一个稍微复杂的 DataFrame 数据集
# data_1 = {
# '评论ID': np.arange(1, 21),
# '评论者': ['用户' + str(i) for i in range(1, 21)],
# '评分': np.random.randint(1, 6, size=20), # 随机生成 1 到 5 的评分
# '电影评论': [
# "这部电影非常好", "剧情很有意思", "演员表现很棒", "非常无聊", "电影节奏太慢", 
# "特效很震撼", "故事情节扣人心弦", "浪费时间", "演员不行", "挺好看的",
# "剧情很感人", "真的是烂片", "音乐很好听", "导演太差了", "电影拍得不错", 
# "没有意思", "剧情平淡", "很喜欢", "不错的电影", "很失望"
# ],
# '评论时间': pd.date_range('2024-01-01', periods=20, freq='D') # 评论时间从2024年1月1日开始
# }

# # 创建 DataFrame
# df_1 = pd.DataFrame(data_1)

# # 补充【1】处代码，打印前10行数据
# print("任务 ① - 前10行数据：")
# print(df_1.head(10))
# #任务一结束
 
import pandas as pd

try:
    data = pd.read_csv('comment_with.csv')
    print(data.head(10))
except FileNotFoundError:
    print("文件 'comment_with.csv' 未找到。")