#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  homework15_1_2.py


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    x_values = list(range(1, 5001))
    y_values = [x**3 for x in x_values]
    
    x_show = x_values[0:5]
    y_show = y_values[0:5]
    
    plt.scatter(x_show, y_show, c=y_show, cmap=plt.cm.Blues, s=40)
    #plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)
    #设置图表标题并给坐标轴加上标签
    plt.title("Cube Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    #设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    #设置每个坐标轴的取值范围
    #plt.axis([0, 5100, 0, 130000000000])
    plt.show()

