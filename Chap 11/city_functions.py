#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_city_country.py

def city_info(city_name, country_name, population = ''):
    neat_name = city_name + ', ' + country_name
    if population:
        city_info = neat_name.title() + ' - population ' + str(population)
    else:
        city_info = neat_name.title()
        
    return city_info
    
 
if __name__ == '__main__':
    city = city_info('wuhan', 'china')
    print(city)
