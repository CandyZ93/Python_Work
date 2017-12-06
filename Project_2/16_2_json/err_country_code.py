#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   err_country_code.py


if __name__ == '__main__':
    with open('no_country_code.txt') as f:
        lines = f.readlines()
        
    for line in lines:
        s_line = line.split()
        if s_line[0] == 'ERROR':
            print(line)
            

