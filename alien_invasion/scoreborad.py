#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    '''显示得分等信息'''

    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = ai_settings
        self.stats = stats

        #设置得分板属性
        self.text_color = (30, 30, 30)
        #create a Font object from the system fonts,SysFont(name, size, bold=False, italic=False) -> Font
        self.font = pygame.font.SysFont(None, 48, True)

        #初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        '''将分数渲染到surface上'''
        rounded_score = round(self.stats.score, -1) #取10的整数倍，比如3212->3210,334->330,如果参数是-2表示取百的整数
        score_str = "{:,}".format(rounded_score)    #使用,作为千位分隔符,比如3212->3,212

        #draw text on a new Surface, render(text, antialias, color, background=None) -> Surface
        #第二个参数if true the characters will have smooth edges
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        #显示到右上角
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def show_score(self):
        '''在屏幕上显示分数'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen) #根据group中每个ship的rect绘制到屏幕上

    def prep_high_score(self):
        '''将最高分数渲染到surface上'''
        rounded_high_score = round(self.stats.high_score, -1) #取10的整数倍，比如3212->3210,334->330,如果参数是-2表示取百的整数
        score_str = "{:,}".format(rounded_high_score)    #使用,作为千位分隔符,比如3212->3,212

        #draw text on a new Surface, render(text, antialias, color, background=None) -> Surface
        #第二个参数if true the characters will have smooth edges
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        #显示到屏幕中央
        self.high_score_rect.top = self.screen_rect.top
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prep_level(self):
        '''在得分下方显示当前等级'''
        #draw text on a new Surface, render(text, antialias, color, background=None) -> Surface
        #第二个参数if true the characters will have smooth edges
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        #显示到得分下方
        self.level_rect.top = self.score_rect.bottom + 10
        self.level_rect.right = self.score_rect.right

    def prep_ship(self):
        '''在屏幕上显示还有多少条飞船'''
        self.ships = Group()
        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.screen, self.settings)
            #显示在屏幕左上角
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 10

            #添加到group中
            self.ships.add(ship)
