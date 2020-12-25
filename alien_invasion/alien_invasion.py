#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''外星人入侵游戏'''

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreborad import Scoreboard

def run_game():
    #初始化游戏，并且创建一个游戏主屏幕

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建游戏统计对象
    stats = GameStats(ai_settings)

    #创建记分板
    scoreborad = Scoreboard(screen, ai_settings, stats)

    #创建play button
    play_button = Button(screen, ai_settings, 'Play')

    #创建一艘飞船
    ship = Ship(screen, ai_settings)

    #创建一个group，用来管理所有发射出的子弹
    bullets = Group()

    #创建一个星人group
    aliens = Group()
    gf.create_fleet(screen, ai_settings, aliens, ship)

    #游戏的主循环
    while True:
        gf.check_events(screen, ai_settings, ship, aliens, bullets, stats, play_button, scoreborad)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, screen, ai_settings, ship, stats, scoreborad)
            gf.update_aliens(screen, ai_settings, aliens,ship, bullets, stats, scoreborad)

        gf.update_screen(screen, ai_settings, ship, bullets, aliens, stats, play_button,
            scoreborad)

run_game()

