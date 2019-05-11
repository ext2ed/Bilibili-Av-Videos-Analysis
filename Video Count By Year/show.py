import pandas as pd
import matplotlib.pyplot as plt
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取数据,分隔符[ ]
data = pd.read_csv("data.txt", header=None, delimiter='	')
# 取数据值
video_counts = data.iloc[:, -1].values
year = data.iloc[:, 0].values
#Mat = data.iloc[:, 0:2]
plt.plot(year, video_counts,alpha=0.8)
# 设置X轴标签
plt.xlabel("年份")
# 设置Y轴标签
plt.ylabel("稿件总数")
# 设置标题
plt.title("BiliBili 投稿视频数量(2009-2019)")
# 增加格点
plt.grid(True)
# 设置x轴刻度
plt.xticks(year)
# 设置数字标签
for a, b in zip(year, video_counts):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig("show.png")
plt.show()