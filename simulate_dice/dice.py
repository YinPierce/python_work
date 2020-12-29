#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

from random import randint

class Dice():
    '''模拟骰子的类'''
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        '''返回一个１到面数之间的整数'''
        return randint(1, self.num_sides)