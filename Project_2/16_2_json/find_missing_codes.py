#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  find_missing_ccodes.py

def search_missing_cname(filename):
    """找到出现错误的国家名"""
    c_list = []
    
    with open(filename) as f:
        c_lines = f.readlines()
        for line in c_lines:
            if line != '\n':
                line = line.strip()
                c_line = line.split('-')
                country_tname = c_line[-1].strip()
                c_list.append(country_tname)
            
        return c_list
        
            
  
if __name__ == '__main__':
    filename = 'countries_need_search.txt'
    country_list = search_missing_cname(filename)
    for cname in country_list:
        print(cname)
