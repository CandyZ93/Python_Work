#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  homework1_add.py


def solid_add():
    while True:
        first_number = input("\nPlease enter the first number('q' for quit):")
        if first_number == 'q':
            break
        second_number = input("Please enter the second number('q' for quit):")
        if second_number == 'q':
            break
        
        try:
            answer = int(first_number) + int(second_number)
        except ValueError:
            print("Make sure you entered 2 numbers!")
        else:
            print("The anser is:" + str(answer))
    

if __name__ == '__main__':
        solid_add()
