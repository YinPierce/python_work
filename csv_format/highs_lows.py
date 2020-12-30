#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

from datetime import datetime
import csv
import matplotlib.pyplot as plt

# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    headrow = next(reader) #将文件的第一行数据读取进来，并且存储到列表中，每个元素是字符串

    # for index, column_header in enumerate(headrow): #enumerate函数用来对可迭代对象进行遍历，返回一个以序列号为键的元组
    #     print(index, column_header)

    #提取每天的最高温度，根据第一行的信息，最高温度在每行的第二列
    dates, highs, lows = [], [], []
    for row in reader:  #上面已经通过next调用访问了第一行，所以这里从第二行开始
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1]) #华氏度
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data.')
        else:
            dates.append(current_date)
            #转换为摄氏度℃=5（F-32）/9 
            high = round(5 * (high-32) / 9) #四舍五入
            highs.append(high)
            low = round(5 * (low-32) / 9) #四舍五入
            lows.append(low)

#绘制最高气温
fig = plt.figure(figsize=(1920, 1080))
plt.plot(dates, highs, c='red', alpha=0.5) #alpha表示透明度，１表示完全不透明，０表示完全透明

#绘制最低气温
plt.plot(dates, lows, c='blue', alpha=0.5)

#用颜色填充两条曲线
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形格式
plt.title('Daily High and Low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=14)
#将x轴的时间使用斜体显示，避免重叠
fig.autofmt_xdate()

plt.ylabel('Temperature (C)', fontsize=14)
#设置坐标轴刻度的字体大小，both表示两个坐标轴
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()