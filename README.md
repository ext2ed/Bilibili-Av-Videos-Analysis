# Bilibili 视频数据分析
![Language](https://img.shields.io/badge/Language-Python-yellowgreen.svg?style=flat-square)
![Data Storage Size](https://img.shields.io/badge/20.66-GB-critical.svg?style=flat-square)
![Data Total Size in Memory](https://img.shields.io/badge/44.77-GB-informational.svg?style=flat-square)

项目块负责
目录 | 作者 | 说明
-|-|-|
Video Count By Year | [@Wuxiexie](https://github.com/WuXieXie) | 年度稿件数量 |
Video Quantity Ranking | [@dirname](https://github.com/dirname) | 投稿数量 Top 50 |
Video Ratio | [@Wuxiexie](https://github.com/WuXieXie) | 稿件有效率 |
Video Tag Ratio | [@Wuxiexie](https://github.com/WuXieXie) | 稿件类型占比 |
Video Tag Ratio By Year | [@Wuxiexie](https://github.com/WuXieXie) | 年度稿件类型占比 |

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


