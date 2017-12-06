#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dice_mplhist.py


if __name__ == '__main__':    
    import matplotlib.pyplot as plt
    
    from die import Die
    
    #创建一个D6和一个D10
    die_1 = Die()
    die_2 = Die(10)
    
    #掷几次骰子， 并将结果存储在一个列表中
    results = []
    
    #使用列表解析代替循环
    results = [ die_1.roll() + die_2.roll() for roll_num in range(50000)]
    
    #分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    v_list = range(2, max_result+1) #记得range方法要将面数+1
    print(v_list)
    
    #使用列表解析代替循环
    frequencies = [ results.count(value) for value in v_list]
    
    # the Barchart of the data
    plt.bar(v_list, frequencies)   
    
    
    plt.xlabel('Result', fontsize=14)
    plt.ylabel('Frequencies', fontsize=14)
    plt.title('Result of rolling D6 + D10 50000 times.', fontsize=16)
    
    #plt.axis([0, 18, 0, 30000])
    
    plt.show()
    
