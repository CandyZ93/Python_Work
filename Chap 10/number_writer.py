#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_writer.py

if __name__ == '__main__':
    import json
    
    numbers = [2, 3, 5, 7, 11, 13]
    
    filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
