#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  game_functions.py
#  
import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
			
def fire_bullet(ai_settings, screen, ship, bullets):
	"""如果还没有达到限制，就发射一颗子弹"""
	# 创建新子弹并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
	
def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	
def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	# 监视键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color) # 先填充背景色后绘制其他元素
	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
		
	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings, bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	# 更新子弹的位置
	bullets.update() # 对编组调用update()，自动对每个精灵调用
	
	# 删除已消失的子弹
	for bullet in bullets.copy(): ### for遍历时不应修改遍历对象！！故遍历副本
		if bullet.rect.left >= ai_settings.screen_width:
			bullets.remove(bullet)
	#print(len(bullets)) # 验证子弹被正确删除，运行不应保留，写入终端拖慢速度
