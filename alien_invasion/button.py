#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame.font

class Button():

    def __init__(self, screen, ai_settings, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) #green
        self.txt_color = (255, 255, 255)
        #create a Font object from the system fonts,SysFont(name, size, bold=False, italic=False) -> Font
        self.font = pygame.font.SysFont(None, 48) 

        #创建rect,并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)   #Rect(left, top, width, height) -> Rect
        self.rect.center = self.screen_rect.center

        #创建按钮的标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''将字符串渲染为图片,并在button的居中显示'''

        #draw text on a new Surface, render(text, antialias, color, background=None) -> Surface
        #第二个参数if true the characters will have smooth edges
        self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制button,先在屏幕上绘制button的矩形，在将字符串绘制上去'''

        #fill Surface with a solid color,fill(color, rect=None, special_flags=0) -> Rect
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)