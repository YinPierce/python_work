#! /usr/bin/env python3
'''外星人入侵游戏'''

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏，并且创建一个游戏主屏幕

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship = Ship(screen, ai_settings)

    #创建一个group，用来管理所有发射出的子弹
    bullets = Group()

    #游戏的主循环
    while True:
        gf.check_events(screen, ai_settings, ship, bullets)
        ship.update_pos()
        gf.update_bullets(bullets)

        gf.update_screen(screen, ai_settings, ship, bullets)

run_game()

