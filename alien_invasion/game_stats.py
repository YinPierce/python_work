#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class GameStats():
    '''游戏的统计信息'''

    def __init__(self, ai_settings):
        #初始化统计信息
        self.settings = ai_settings
        self.reset_stats()
        self.game_active = False
        #从文件中读取历史最高分
        try:
            with open(ai_settings.high_score_file) as file_object:
                high_score_str = file_object.read()
                self.high_score = int(high_score_str)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        #初始化在运行期间可能变化的统计信息
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
