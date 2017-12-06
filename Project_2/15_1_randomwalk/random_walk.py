#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  random_walk.py

from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        
        #所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def get_step(self):
        """获取轴向步长"""
        axis_range = list(range(8))
        direction = choice([1, -1])
        distance = choice(axis_range)
        axis_step = direction * distance
        return axis_step
        
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        #不断漫步，直到列表到达指定的长度
        #x_range = list(range(8))
        #y_range = list(range(8))
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            '''x_direction = choice([1, -1])
            x_distance = choice(x_range)
            x_step = x_direction * x_distance'''
            x_step = self.get_step()
                        
            '''y_direction = choice([1, -1])
            y_distance = choice(y_range)
            y_step = y_direction * y_distance'''
            y_step = self.get_step()
            
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
                
            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)       
        
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
