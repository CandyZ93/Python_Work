#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  my_electric_car.py

from class_car_Inheritance import ElectricCar

if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
