#! /usr/bin/env python3

import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, screen, ai_settings, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #右移飞船
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        #空格键表示开火，发射一个子弹
        fire_bullets(screen, ai_settings, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
            ship.move_right = False
    elif event.key == pygame.K_LEFT:
            ship.move_left = False

def check_events(screen, ai_settings, ship, bullets):
    #监视键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ai_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(screen, settings, ship, bullets):
    #每帧都要重新绘制
    screen.fill(settings.bg_color)
    ship.blitme()

    #绘制所有子弹, group.sprites->list of the Sprites this Group contains
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #让最新的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(screen, ai_settings, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        bullet = Bullet(screen, ai_settings, ship)
        bullets.add(bullet)