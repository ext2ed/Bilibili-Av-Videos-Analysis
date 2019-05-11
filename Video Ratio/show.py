import pandas as pd
import matplotlib.pyplot as plt
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
wedges, texts, autotexts = plt.pie(video_counts,explode=explode,shadow=True,autopct='%1.2f%%',pctdistance=0.8)
# 设置标题
plt.title("BiliBili 稿件有效率")
plt.legend(wedges, type,
          title="稿件状态",
          loc="center left",
          bbox_to_anchor=(0.85,0))
# 设置数字标签
# for a, b in zip(type, video_counts):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig("show.png")
plt.show()