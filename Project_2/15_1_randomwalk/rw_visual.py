#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rw_visual.py

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    from random_walk import RandomWalk
    
    #只要程序处于活动状态， 就不断地模拟随机漫步
    while True:
        #创建一个RandomWalk实例， 并将其包含的点都绘制出来
        rw = RandomWalk(5000)
        rw.fill_walk()
        
        #设置绘图窗口的尺寸
        plt.figure(figsize=(10, 6))
        point_numbers = list(range(rw.num_points))
        #range()生成数字列表，用于每个点的颜色映射
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
        cmap=plt.cm.Blues, s=1) #c=, cmap=进行颜色映射
        #plt.plot(rw.x_values, rw.y_values, linewidth=1)
        
        #突出起点和终点
        plt.scatter(0, 0, c='green', s=50)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)
                
        #隐藏坐标轴， 确保本部分代码放在plt.show()之前
        #plt.axes().get_xaxis().set_visible(False)
        #plt.axes().get_yaxis().set_visible(False)
        
        plt.show()
        
        keep_running = input("Make another walk?(y/n): ")
        if keep_running == 'n':
            break
            
