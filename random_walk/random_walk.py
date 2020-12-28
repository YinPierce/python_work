#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

'''模拟随机漫步'''

from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        #起始点从（０，０）开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算并存储随机漫步的点'''
        while len(self.x_values) < self.num_points:
            #决定本次移动的方向和距离
            x_step = self.get_walk_step()
            y_step = self.get_walk_step()

            #计算这一步达到的点，以作为下一步的起始点
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_walk_step(self):
        direction = choice([1, -1]) #x方向向左或右,y向上或者向下
        distance = choice([0, 1, 2, 3, 4]) #从这个列表中随机返回一个值，０，表示只沿着其中一个轴移动
        step = direction * distance
        return step