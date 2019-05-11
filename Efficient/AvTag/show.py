import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取数据,分隔符[ ]
data = pd.read_csv("data.txt", header=None, delimiter='	')
# 取数据值
video_counts = data.iloc[:, -1].values
type = data.iloc[:, 0].values
#Mat = data.iloc[:, 0:2]
explode=tuple([0.1] * len(type))
# 设置尺寸
plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(video_counts,labels=type,explode=explode,shadow=True,autopct='%1.2f%%',pctdistance=0.8)
# 设置标题
plt.title("BiliBili 稿件分类占比")
# 设置数字标签
# for a, b in zip(type, video_counts):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig("show.png")
plt.show()