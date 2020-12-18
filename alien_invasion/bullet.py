#! /usr/bin/env python3

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''描述子弹的类'''

    def __init__(self, screen, ai_settings, ship):
        super().__init__()

        self.screen = screen
        
        #创建一个rect, Rect(left, top, width, height)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数表示子弹的位置，子弹只会沿着y方向移动
        self.f_y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''子弹向上移动,感觉是重写了父类sprite的update函数，这个函数会被sprite.group.update调用'''
        self.f_y -= self.speed_factor
        self.rect.y = self.f_y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect) #rect(surface, color, rect)