#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #创建一个RandomWalk实例，并将它的所有点绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    #设置窗口尺寸
    plt.figure(figsize=(1920, 1080))

    #利用颜色映射，按照步行先后顺序，颜色由浅变深
    point_nums = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plt.cm.Blues, edgecolor='none', s=1)

    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s = 50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s = 50)

    #隐藏x,y坐标轴
    #axes:Add an axes to the current figure and make it the current axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False) #这种方式会报warning:MatplotlibDeprecationWarning

    #gca:Get the current axes, creating one if necessary.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_going = input('Make another walk? (y/n):')
    if keep_going == 'n':
        break