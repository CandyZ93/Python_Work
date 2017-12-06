#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  my_cars.py
'''
from class_car_Inheritance import Car, ElectricCar

if __name__ == '__main__':
   my_beetle = Car('volkswagen', 'beetle', 2016)
   print(my_beetle.get_descriptive_name())
   
   my_tesla = ElectricCar('tesla', 'roadster', 2016)
   print(my_tesla.get_descriptive_name())
'''

import class_car_Inheritance

my_beetle = class_car_Inheritance.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = class_car_Inheritance.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
