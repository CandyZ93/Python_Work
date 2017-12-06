#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rw_pygal.py


if __name__ == '__main__':
    import pygal
    
    from random_walk import RandomWalk
    
    #只要程序处于活动状态， 就不断地模拟随机漫步
    while True:
        #创建一个RandomWalk实例， 并将其包含的点都绘制出来
        rw = RandomWalk(5000)
        rw.fill_walk()
        coordinates = [(x, y) for x, y in zip(rw.x_values, rw.y_values)]
        
        rw_xy_chart = pygal.XY(stroke=False)
        rw_xy_chart.title = 'RandomWalk'
        rw_xy_chart.add('Start', [(0, 0)])
        rw_xy_chart.add('Walk', coordinates)
        rw_xy_chart.add('End', [(rw.x_values[-1], rw.y_values[-1])])
        
        rw_xy_chart.render_to_file('rw_pygal.svg')
        
        keep_running = input("Make another walk?(y/n): ")
        if keep_running == 'n':
            break
