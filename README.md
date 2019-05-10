# Bilibili 视频数据分析
本项目是使用 Redis + Scrapy 开发的集群式爬虫, 爬取了视频 Av 号 __1 - 51746026__ 的所有视频信息
- [Spider 爬虫](#Spider-爬虫)
    - [爬虫环境](#爬虫环境)
    - [工作流程](#工作流程)

## Spider 爬虫
使用 Redis 管理递增 Av 号, 能减少网络堵塞等特定情况下数据的遗漏, 并允许多台机器同时工作爬行

### 爬虫环境
+ MongoDB Community 4.0
+ Scrapy 1.5.2
+ Redis 5.0.3
+ Python 3.7.3
+ CentOS 7

### 工作流程

![Spider chart](flow-chart.png)


