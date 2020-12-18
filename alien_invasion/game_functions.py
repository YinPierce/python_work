#! /usr/bin/env python3

import sys
import pygame

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        #右移飞船
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
            ship.move_right = False
    elif event.key == pygame.K_LEFT:
            ship.move_left = False

def check_events(ship):
    #监视键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(screen, settings, ship):
    #每帧都要重新绘制
    screen.fill(settings.bg_color)
    ship.blitme()

    #让最新的屏幕可见
    pygame.display.flip()