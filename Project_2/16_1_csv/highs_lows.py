#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  highs_lows.py



if __name__ == '__main__':
    import csv
    from datetime import datetime
    
    from matplotlib import pyplot as plt
    
    #从文件中获取日期、最高气温和最低气温
    filename = 'sitka_weather_2014.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader) #阅读器读取头行--停留在第二行，便于后续读取
        #print(header_row)
        
        #enumerate()获取每个元素的索引及值
        #~ for index, column_header in enumerate(header_row):
            #~ print(index,column_header)
            
        dates, highs, lows = [], [], []
        
        for row in reader:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            #strptime方法接受-分隔的字符串和解释格式
            dates.append(current_date)
            high = int(row[1]) #将读出的字符串转为数字
            highs.append(high)
            low = int(row[3])
            lows.append(low)
        
                
    #根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red') #最高气温图表
    plt.plot(dates, lows, c='blue') #最低气温图表
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)
    #给图表区域着色
    
    #设置图形的格式
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() #fig.autofmt_xdate()方法绘制斜的日期标签 避免重叠
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    #设置坐标轴的取值范围
    plt.ylim((0,120)) #plt.ylim((low,high))方法
    
    plt.show() 
    
