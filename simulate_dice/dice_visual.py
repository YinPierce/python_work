#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

import pygal

from dice import Dice

dice6 = Dice()
dice6_2 = Dice()

results = []
for x in range(1000):
    result = dice6.roll() + dice6_2.roll()
    results.append(result)

#分析结果
frequencies = []
for x in range(2, dice6.num_sides + dice6_2.num_sides +1):
    frequency = results.count(x)
    frequencies.append(frequency)

#可视化每个点的频率
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(2, dice6.num_sides + dice6_2.num_sides +1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_2_visual.svg')

