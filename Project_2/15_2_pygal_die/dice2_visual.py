#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dice2_visual.py


if __name__ == '__main__':
    import pygal
    
    from die import Die
    
    #创建两个D8
    die_1 = Die(8)
    die_2 = Die(8)
    
    #掷几次骰子， 并将结果存储在一个列表中
    results = []
    for roll_num in range(10000000):
        result = die_1.roll() + die_2.roll()
        results.append(result)
        
    #分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    v_list = range(2, max_result+1) #记得range方法要将面数+1
    print(v_list)
    for value in v_list:
        frequency = results.count(value)
        frequencies.append(frequency)
    
    #对结果进行可视化
    hist = pygal.Bar()#创建一个pygal.Bar()实例并存储在hist中
    
    hist.title = "Results of rolling two D8 10000000 times."
    #hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = list(map(str, v_list))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    hist.add('D8 + D8', frequencies)
    hist.render_to_file('dice2_visual.svg')
    
    #print(frequencies)

