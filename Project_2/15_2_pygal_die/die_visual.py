#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  die_visual.py


if __name__ == '__main__':
    import pygal
    
    from die import Die
    
    #创建一个D6
    die = Die()
    
    #掷几次骰子， 并将结果存储在一个列表中
    results = []
    for roll_num in range(100000):
        result = die.roll()
        results.append(result)
        
    #分析结果
    frequencies = []
    v_list = range(1, die.num_sides+1) #记得range方法要将面数+1
    for value in v_list:
        frequency = results.count(value)
        frequencies.append(frequency)
    
    #对结果进行可视化
    hist = pygal.Bar()#创建一个pygal.Bar()实例并存储在hist中
    
    hist.title = "Results of rolling one D6 1000 times."
    #hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = list(map(str, v_list))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    hist.add('D6', frequencies)
    hist.render_to_file('die_visual.svg')
    
    print(frequencies)
