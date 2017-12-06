#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  three_dices.py


if __name__ == '__main__':
    import pygal
    
    from die import Die
    
    #创建三个D6
    die_1 = Die()
    die_2 = Die()
    die_3 = Die()
    
    #掷几次骰子， 并将结果存储在一个列表中
    results = []
    '''for roll_num in range(100000):
        result = die_1.roll() + die_2.roll()
        results.append(result)'''
    #使用列表解析代替循环
    results = [ die_1.roll() + die_2.roll() + die_3.roll()\
     for roll_num in range(500000)]
        
    #分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    v_list = range(3, max_result+1) #记得range方法要将面数+1
    print(v_list)
    '''for value in v_list:
        frequency = results.count(value)
        frequencies.append(frequency)'''
    #使用列表解析代替循环
    frequencies = [ results.count(value) for value in v_list]
        
    
    #对结果进行可视化
    hist = pygal.Bar()#创建一个pygal.Bar()实例并存储在hist中
    
    hist.title = "Results of rolling three D6 50000 times."
    #hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = list(map(str, v_list))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    hist.add('3 D6', frequencies)
    hist.render_to_file('three_dices_visual.svg')
    
    #print(frequencies)
