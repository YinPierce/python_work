#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''描述外星人的类'''

    def __init__(self, screen, ai_settings):
        super().__init__()

        self.screen = screen
        self.settings = ai_settings

        #加载位图，创建alien自己的surface
        self.image = pygame.image.load('images/alien.bmp')

        #确定自己的初始位置，默认为屏幕左上角附近
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.f_x = float(self.rect.x) #x坐标位置,用浮点数存储，提高精度

    def blitme(self):
        '''将本身绘制到screen上'''
        self.screen.blit(self.image, self.rect) #blit(source, dest, area=None, special_flags=0)

    def update(self):
        '''外星人移动,重写了父类sprite的update函数，这个函数会被sprite.group.update自动调用'''
        self.f_x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.f_x

    def check_edges(self):
        '''如果外星人已经移动到屏幕边缘，返回True，用来控制外星人的移动方向'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
