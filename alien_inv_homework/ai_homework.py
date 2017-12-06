#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alien_invasion.py
#

import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	
	# 开始游戏的主循环
	while True:
		# 先检测键盘事件再更新飞船、子弹编组状态，传入子弹编组！
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update() # 先更新飞船状态再绘制
		gf.update_bullets(ai_settings, bullets)				
		gf.update_screen(ai_settings, screen, ship, bullets)
		
run_game()