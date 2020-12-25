#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''描述飞船的类'''

    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.settings = ai_settings

        #加载位图，创建ship自己的surface
        self.image = pygame.image.load('images/ship.bmp')

        #根据screen的rect，决定自己的位置，默认为屏幕最下方正中间
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.f_center = float(self.screen_rect.centerx) #x中心坐标位置,用浮点数存储，飞船移动位置提高精度
        self.rect.bottom = self.screen_rect.bottom #y坐标
        self.move_right = False
        self.move_left = False
        self.rect.centerx = self.f_center

    def blitme(self):
        '''将飞船本身绘制到screen上'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.f_center += self.settings.ship_speed_factor

        if self.move_left and self.rect.left > self.screen_rect.left:
            self.f_center -= self.settings.ship_speed_factor

        self.rect.centerx = self.f_center

    def center_ship(self):
        self.f_center = self.screen_rect.centerx