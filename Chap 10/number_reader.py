#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_reader.py

if __name__ == '__main__':
    import json
    
    filename = 'numbers.json'
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
        
        print(numbers)
