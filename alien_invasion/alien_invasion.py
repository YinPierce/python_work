#! /usr/bin/env python3
'''外星人入侵游戏'''

import pygame

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

    #游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update_pos()
        gf.update_screen(screen, ai_settings, ship)

run_game()

