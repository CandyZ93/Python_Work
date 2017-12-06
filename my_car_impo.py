#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  my_car_impo.py

from class_car_Inheritance import Car


if __name__ == '__main__':
    my_new_car = Car('audi', 'a4', 2016)    
    print(my_new_car.get_descriptive_name())
    
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
