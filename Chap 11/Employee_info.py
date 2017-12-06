#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Employee.py

class Employee():
    """记录雇员的信息和年薪"""
    def __init__(self, first_name, last_name, income):
        self.first_name = first_name
        self.last_name = last_name
        self.income = income
    
    def give_raise(self, amount = 5000):
        self.income += amount
        

if __name__ == '__main__':
    Jack = Employee('Jack', 'Ma', 1000000)
    print(Jack.income)
    Jack.give_raise()
    print(Jack.income)
    Jack.give_raise(100000)
    print(Jack.income)
    
