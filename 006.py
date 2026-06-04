import pandas as pd

try:
    data = pd.read_csv('comment_with.csv')
    print(data['电影评论'])
except FileNotFoundError:
    print("文件 'comment_with.csv' 未找到。")



# #任务二
# import pandas as pd
# import numpy as np
# # 创建一个稍微复杂的 DataFrame 数据集
# data_2 = {
# '评论ID': np.arange(1, 21),
# '评论者': ['用户' + str(i) for i in range(1, 21)],
# '评分': np.random.randint(1, 6, size=20), # 随机生成 1 到 5 的评分
# '电影评论': [
# "剧情复杂", "演员演技很差", "好看的电影", "情节拖沓", "情感细腻", 
# "非常喜欢这部电影", "电影拍得太慢", "没有亮点", "剧情没有意义", "电影好评",
# "演技不错", "情节非常紧张", "特效差", "评分不高", "剧情很普通", 
# "非常感人", "真心不好看", "导演很棒", "制作精良", "期待续集"
# ],
# '评论时间': pd.date_range('2024-01-01', periods=20, freq='D') # 评论时间从2024年1月1日开始
# }
# # 创建 DataFrame
# df_2 = pd.DataFrame(data_2)
# # 补充【2】处代码，打印“电影评论”一列
# print("\n任务 ② - 电影评论列：")
# print(df_2['电影评论'])
# #任务二结束