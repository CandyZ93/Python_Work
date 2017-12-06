#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2_dices_multiply.py

def get_values(num1, num2):
    values = []
    for n1 in range(1, num1+1):
        for n2 in range(1, num2+1):
            values.append(n1*n2)
    
    value_list = list(set(values))
    value_list.sort()
    return value_list
    
    
if __name__ == '__main__':
    import pygal
    
    from die import Die
    
    #创建两个D6
    die_1 = Die()
    die_2 = Die()
    
    #掷几次骰子， 并将结果存储在一个列表中
    #results = [] 列表解析不需要初始化列表
    '''for roll_num in range(500000):
        result = die_1.roll() * die_2.roll()
        results.append(result)'''
    #使用列表解析替换循环
    results = [die_1.roll()*die_2.roll() for roll_num in range(50000)]
        
    #分析结果
    #frequencies = [] 列表解析不需要初始化列表
    #max_result = die_1.num_sides * die_2.num_sides
    #v_list = range(2, max_result+1) #记得range方法要将面数+1
    v_list = get_values(die_1.num_sides, die_2.num_sides)
    print(v_list)
    '''for value in v_list:
        frequency = results.count(value)
        frequencies.append(frequency)'''
    #使用列表解析替换循环
    frequencies = [results.count(value) for value in v_list]
    
    #对结果进行可视化
    hist = pygal.Bar()#创建一个pygal.Bar()实例并存储在hist中
    
    hist.title = "Results of rolling two D6 500000 times."
    #hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = list(map(str, v_list))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    
    hist.add('D6 * D6', frequencies)
    hist.render_to_file('2dice_multiply_visual.svg')
    
    #print(frequencies)
