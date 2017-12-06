#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  greet_user.py
#  

if __name__ == '__main__':
    import json
    
    filename = 'username.json'
    
    with open(filename) as f_obj:
        username = json.load(f_obj)
        print("Welcome back, " + username + "!")
        
