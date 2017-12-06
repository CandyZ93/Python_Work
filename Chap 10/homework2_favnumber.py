#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  homework2_favnumber.py


def get_stored_favnum():
    """如果存储了喜欢的数字，就获取它"""
    filename = 'favnumber.txt'
    try:
        with open(filename) as f_obj:
            favnum = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favnum
def get_new_favnum():
    """提示输入喜欢的数字"""
    favnum = input("Pleas input your favorite number. ")
    filename = 'favnumber.txt'
    with open(filename, 'w') as f_obj:
        json.dump(favnum, f_obj)
    return favnum

def show_favnum():
    """打印喜欢的数字"""
    favnum = get_stored_favnum()
    if favnum:
        print("I know your favorite number! It's " + str(favnum) +"!")
    else:
        favnum = get_new_favnum()
        print("Your favorite number is " + str(favnum) +". I'll remember it.")
        
        
if __name__ == '__main__':
    import json
    show_favnum()
