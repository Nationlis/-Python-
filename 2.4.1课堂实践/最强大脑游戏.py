# P021 任务二：用Python语言实现游戏
# 最强大脑游戏

import random                                 # 导入三个模块:1.随机数
import time                                   # 2.时间函数
import os                                     # 3.操作系统
print("你好,现在你有10秒的时间记忆下列物品及其编号")  # 给出提示
things = ["苹果","香蕉","橙子","梨子","猕猴桃","柚子",
          "猴魁","铁观音","彩蛋","复活节"]    # 定义物品列表
for i in range(10):
    print(i + 1, ":", things[ i ] )           # 在屏幕上打印序号和列表元素
time.sleep( 5 )                               # 等待5秒
os.system( "cls" )                            # 调用操作系统功能：清屏
n = 0                                         # 答对的题数初始为0
t2 =  random.sample( things, 5 )              # 从物品things列表中随机抽取5个物品
for i in t2:
    ans = int( input(i + "的编号是:"))
    if i== things[ ans -1 ]:
        n = n + 1                             # 5件物品中回答正确，就加1
print( "\n你一共答对了", n, "次" )            # 屏幕上显示回答正确的题数
input( "\n按回车键结束" )


