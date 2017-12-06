#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  world_gdp.py


def get_data_of_year(GDP_data, q_year):
    """获得该年的数据并存入列表"""
    GDPs = {}
    for GDP_dict in GDP_data:
        if GDP_dict['Year'] == q_year:  #本数据集'Year'字段是整数而非字串
            country_name = GDP_dict['Country Name']
            GDP = int(float(GDP_dict['Value']))
            code = get_country_code(country_name)
            if code:
                GDPs[code] = GDP/1000000000
    
    return GDPs
        
if __name__ == '__main__':
    import json
    
    import pygal
    from pygal.style import LightColorizedStyle as LCS, \
    RotateStyle as RS
    
    
    from country_codes import get_country_code
        
    #将数据加载到一个列表中
    filename = 'gdp_json.json'
    with open(filename) as f:
        GDP_data = json.load(f)
        
    #打印每个国家2010年的GDP
    q_year = 2015
    cc_GDPs = get_data_of_year(GDP_data, q_year)
    #print(cc_GDPs)
            
    #根据GDP将所有的国家分成三组
    cc_GDPs_1, cc_GDPs_2, cc_GDPs_3 = {}, {}, {}
    for cc, GDP in cc_GDPs.items():
        if GDP < 1000:
            cc_GDPs_1[cc] = GDP
        elif GDP < 10000:
            cc_GDPs_2[cc] = GDP
        else:
            cc_GDPs_3[cc] = GDP
            
    #看看每组分别包含多少国家
    print(len(cc_GDPs_1), len(cc_GDPs_2), len(cc_GDPs_3))
    
    #设置颜色和基本样式
    wm_style = RS('#336699', base_style=LCS)
      
    wm = pygal.maps.world.World(style=wm_style)
    wm.title = 'World GDP(billions) in ' + str(q_year) + ', by Country'
    wm.add('0-1000bn', cc_GDPs_1)
    wm.add('1000bn-10000bn', cc_GDPs_2)
    wm.add('>10000bn', cc_GDPs_3)
    
    #wm.add('2010', cc_GDPs)
    
    wm.render_to_file('world_gdp.svg')
