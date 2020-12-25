#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def record_high_score(ai_settings, stats):
    '''将最高分记录到文件中'''
    with open(ai_settings.high_score_file, 'w') as file_object:
        high_score_str = str(stats.high_score)
        file_object.write(high_score_str)

def check_keydown_events(event, screen, ai_settings, ship, bullets, stats):
    if event.key == pygame.K_RIGHT:
        #右移飞船
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        #空格键表示开火，发射一个子弹
        fire_bullets(screen, ai_settings, ship, bullets, stats)
    elif event.key == pygame.K_q:
        record_high_score(ai_settings, stats)
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
            ship.move_right = False
    elif event.key == pygame.K_LEFT:
            ship.move_left = False

def check_events(screen, ai_settings, ship, aliens, bullets, stats, play_button, sb):
    #监视键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            record_high_score(ai_settings, stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ai_settings, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, ai_settings, aliens, ship, bullets, stats, play_button, mouse_x, mouse_y, sb)

def check_play_button(screen, ai_settings, aliens, ship, bullets, stats, play_button, mouse_x, mouse_y, sb):
    '''检测鼠标是否单击了play按钮'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: #test if a point is inside a rectangle
        #重置游戏动态设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        sb.prep_score()
        # sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()
        stats.game_active = True

        #清空子弹和外星人
        bullets.empty()
        aliens.empty()

        #创建一组新的外星人，飞船居中
        create_fleet(screen, ai_settings, aliens, ship)
        ship.center_ship()


def update_screen(screen, settings, ship, bullets, aliens, stats, play_button, scoreborad):
    #每帧都要重新绘制
    screen.fill(settings.bg_color)
    ship.blitme()

    #绘制所有子弹, group.sprites->list of the Sprites this Group contains
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # alien.blitme()
    aliens.draw(screen) #Draws the contained Sprites to the Surface argument,位置由每个sprite的rect决定

    scoreborad.show_score()

    if not stats.game_active:
        play_button.draw_button()

    #让最新的屏幕可见
    pygame.display.flip()

def update_bullets(bullets, aliens, screen, ai_settings, ship, stats, sb):
    bullets.update()

    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(bullets, aliens, screen, ai_settings, ship,
        stats, sb)

def check_bullet_alien_collisions(bullets, aliens, screen, ai_settings, ship, stats, sb):
    #检查是否有子弹击中了外星人，若击中，删除外星人和子弹
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) #返回一个字典，字典作为键，击中的外星人(list)作为值,
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_point * len(aliens)    #一个子弹有可能击中多个外星人，所以是列表中的个数
        sb.prep_score()
        check_high_score(stats, sb)

    #检查是否所有外星人被射杀，如果是，需要重新创建一群外星人
    if len(aliens) == 0:
        bullets.empty()
        #加快游戏进度
        ai_settings.increase_speed()

        #提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(screen, ai_settings, aliens, ship)
        

def check_high_score(stats, sb):
    '''判断是否有新的最高分，有的话显示它'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def fire_bullets(screen, ai_settings, ship, bullets, stats):
    if not stats.game_active:
        return

    if len(bullets) < ai_settings.bullets_allowed:
        bullet = Bullet(screen, ai_settings, ship)
        bullets.add(bullet)

def get_num_aliens_x(ai_settings, alien_width):
    #计算一行可以容纳几个外星人，间距为外星人的宽
    available_space_x = ai_settings.screen_width - 2 * alien_width #两边各留出一个外星人宽的空间
    num_aliens_x = int(available_space_x / (2 * alien_width))
    return num_aliens_x

def create_alien(screen, ai_settings, aliens, alien_num, alien_row):
    '''创建一个外星人，并将其放入当前行(group)中'''
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.f_x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.f_x

    alien_height = alien.rect.height
    alien.rect.y = alien_height + 2 * alien_height * alien_row

    aliens.add(alien)

def get_num_alien_rows(ai_settings, alien_height, ship_height):
    '''计算屏幕上外星人能放多少行,行间距是外星人的高'''
    #去除第一行外星人的高，ship的高以及ship和外星人之间空两行ship的高
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    num_aliens_rows = int(available_space_y / (2 * alien_height))
    return num_aliens_rows

def create_fleet(screen, ai_settings, aliens, ship):  #aliens是pygame的group
    '''创建外星人群'''

    #计算一行可以容纳几个外星人，间距为外星人的宽
    alien = Alien(screen, ai_settings)
    num_aliens_x = get_num_aliens_x(ai_settings, alien.rect.width)
    num_alien_rows = get_num_alien_rows(ai_settings, alien.rect.height, ship.rect.height)

    #创建一行外星人
    for row in range(num_alien_rows):
        for alien_num in range(num_aliens_x):
            create_alien(screen, ai_settings, aliens, alien_num, row)

def check_fleet_edges(ai_settings, aliens):
    '''检查部队中是否有外星人碰到边缘，是，需要向下移动，并改变移动方向'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(screen, ai_settings, aliens, ship, bullets, stats, sb):
    check_fleet_edges(ai_settings, aliens)

    aliens.update() #pygame的group，这个函数会自动调用内部各个sprinte的update函数

    #检测外星人是否和飞船碰撞
    #spritecollideany(sprite, group, collided = None) -> Sprite Collision with the returned sprite.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, ai_settings, ship, bullets, aliens, stats, sb)

    check_aliens_bottom(screen, ai_settings, ship, bullets, aliens, stats, sb)

def ship_hit(screen, ai_settings, ship, bullets, aliens, stats, sb):
    '''飞船被外星人撞到后'''
    #次数减１
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #更新飞船剩余数
        sb.prep_ship()

        #清空所有显示
        bullets.empty()
        aliens.empty()

        #创建一群新的外星人,飞船居中显示
        create_fleet(screen, ai_settings, aliens, ship)
        ship.center_ship()

        #暂停一会儿，让用户知道飞船已经被撞击
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(screen, ai_settings, ship, bullets, aliens, stats, sb):
    '''检查外星人是否达到屏幕底部，是，停止游戏，等效于撞到飞船'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(screen, ai_settings, ship, bullets, aliens, stats, sb)
            break
