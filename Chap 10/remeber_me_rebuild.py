#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  remember_me_rebuild.py



def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
        
def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        checkflag = input(username + 
        " is logging now. If this is not you enter 'not me'. ")
        if checkflag == 'not me':
            username = get_new_username()
            print("Come back again, " + username + ". We'll remember you.")
        else:
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remeber you when you come back, " + username + "!")

if __name__ == '__main__':
    import json
    
    greet_user()
