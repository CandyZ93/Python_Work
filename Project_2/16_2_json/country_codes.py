#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  countries.py

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #处理两处间名称不一致的国家
    if country_name == 'Bolivia':
        return 'bo'
    elif country_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif country_name == 'Congo, Rep.':
        return 'cg'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Gambia, The':
        return 'gm'
    elif country_name == 'Hong Kong SAR, China':
        return 'hk'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kp'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Lao PDR':
        return 'la'
    elif country_name == 'Libya':
        return 'ly'
    elif country_name == 'Macao SAR, China':
        return 'mo'
    elif country_name == 'Macedonia, FYR':
        return 'mk'
    elif country_name == 'Moldova':
        return 'md'
    elif country_name == 'Slovak Republic':
        return 'sk'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Yemen, Rep.':
        return 'ye'
    
    
    #如果没有找到指定的国家，就返回None
    return None
        


if __name__ == '__main__':
    
    #按字母顺序打印国别码及其对应的国家
    for country_code in sorted(COUNTRIES.keys()):
        print(country_code, COUNTRIES[country_code])
    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))
    print(get_country_code('Afghanistan'))
    print(get_country_code('China'))
    
