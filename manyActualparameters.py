#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#many actual parameters
'''
def make_pizza(size, *toppings):
	"""print all the topping"""
	print("\nMaking a " + str(size) +
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

	
make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
	"""creat a dict, which contain all the info mation about users."""
	profile = {}
	profile['first_name'] =  first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert', 'einstein', 
							 location = 'princeton',
							 filed = 'physics')

print(user_profile)
'''

##homework
'''
def ordered_sandwich(*ingredients):
	flavor = ''
	for ingredient in ingredients:
		flavor += (ingredient + ', ')
	print("You have orderd a " + flavor + "\b\b sandwich.\n")

ordered_sandwich('tuna')
ordered_sandwich('tuna', 'beef')
ordered_sandwich('tuna', 'beef', 'eggroll')

def build_profile(first, last, **user_info):
	"""creat a dict, which contain all the info mation about users."""
	profile = {}
	profile['first_name'] =  first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
person = build_profile('lance', 'zhou', location = 'wuhan', edcation = 'master',
				major = 'software engineering')

full_name = person['first_name'] + ' ' + person['last_name']
print("The profile of " + full_name.title() + " is:")
for k,v in person.items():
	print("\t"+k + " : " +v.title())
'''

def make_car(manufacturer, model, **details):
	car = {}
	car['manufacturer_name'] = manufacturer
	car['model'] = model
	for key,value in details.items():
		car[key] = value
	return car

car = make_car('subaru', 'outback', color = 'red', drive = '4WD')
print(car)
