#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reason_for_programming.py

file_name = 'reasons_for_programming.txt'

def reasons():
    flag = True
    while flag:
        reason = input("Please type in the reason why you programming."+ 
        "\(Enter 'Quit' to quit)\n")
        if reason == 'Quit':
            flag = False
        elif reason == '':
            print("Null is not acceptable!")
        else:
            with open(file_name, 'a') as file_object:
                file_object.write(reason + '\n')

reasons()
        
