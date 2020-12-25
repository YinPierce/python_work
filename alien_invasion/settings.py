#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Settings():
    '''存储外星人入侵游戏中所有设置的类'''
    def __init__(self):
        #主窗口设置
        self.screen_width = 1480
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        self.high_score_file = "./high_score_history.txt"

        #飞船设置
        self.ship_limit = 3

        #子弹的设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #外星人的设置
        self.alien_drop_speed = 10 #向下移动的速度
        self.fleet_direction = 1 #部队的左右移动方向，１向右，-1向左

        self.speedup_scale = 1.1    #以多快的速度加快游戏进度
        self.score_scale = 1.5  #分数增加的速度
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化游戏动态属性，即随着游戏的进行，有些参数会变化，用来提升游戏难度'''
        self.ship_speed_factor = 1.5 #控制飞船的移动速度
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 10 #外星人的移动速度
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)