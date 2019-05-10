import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("sort.txt", header=None, delimiter='	')
video_counts = data.iloc[:, -1].values
up_name = data.iloc[:, 1].values
Mat = data.iloc[:, 0:3]
print(up_name)

idx = np.arange(len(video_counts))
fig = plt.figure(figsize=(19, 10))
plt.barh(idx, video_counts, color='#ffa556', alpha=0.7)
plt.yticks(idx + 0.4, up_name)
plt.grid(axis='x')
plt.xlabel('')
plt.ylabel('')
plt.title('投稿数量 Top 50')
plt.savefig("show.png")
plt.show()
