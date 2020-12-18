#! /usr/bin/env python3

class Settings():
    '''存储外星人入侵游戏中所有设置的类'''
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5 #控制飞船的移动速度
