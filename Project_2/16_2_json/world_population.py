#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  world_population.py


if __name__ == '__main__':
    
    import json
    
    import pygal
    from pygal.style import LightColorizedStyle as LCS, \
    RotateStyle as RS
    
    
    from country_codes import get_country_code
        
    #将数据加载到一个列表中
    filename = 'population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)
        
    #创建一个包含人口数量的字典
    cc_populations = {}
    
    #打印每个国家2010年的人口数量
    q_year = '2010'
    for pop_dict in pop_data:
        if pop_dict['Year'] == q_year:
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value'])) 
            #存在插值得出的浮点数，不能直接int()
            code = get_country_code(country_name)
            if code:
                #print(code + ": " + str(population))
                cc_populations[code] = population
            #~ else:
                #~ print('ERROR - ' + country_name)
                 
            #print(country_name + ': ' + str(population))
            
    #根据人口数量将所有的国家分成三组
    cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
    for cc, pop in cc_populations.items():
        if pop < 10000000:
            cc_pops_1[cc] = pop
        elif pop < 1000000000:
            cc_pops_2[cc] = pop
        else:
            cc_pops_3[cc] = pop
            
    #看看每组分别包含多少国家
    #~ print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
    
    #设置颜色和基本样式
    wm_style = RS('#336699', base_style=LCS)
      
    wm = pygal.maps.world.World(style=wm_style)
    wm.title = 'World Population in ' + q_year + ', by Country'
    wm.add('0-10m', cc_pops_1)
    wm.add('10m-1bn', cc_pops_2)
    wm.add('>1bn', cc_pops_3)
    
    #wm.add('2010', cc_populations)
    
    wm.render_to_file('world_population.svg')
