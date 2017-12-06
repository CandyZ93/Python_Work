#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pizza.py
def make_pizza(size, *toppings):
	"""brief the pizza you want to make"""
	print("\nMaking a " + str(size) + 
			"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

