#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bar_descriptions.py


if __name__ == '__main__':
    import pygal
    from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
    
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    
    chart.title = 'Python Projects'
    chart.x_labels = ['httpie', 'django' , 'flask']
    
    plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.' },
    {'value': 15028, 'label': 'Description of django.' },
    {'value': 14798, 'label': 'Description of flask.' },
    ] #pygal根据'value'键相关联的值来确定高度，与'label'相关联的字符串给条型创建工具提示
    
    chart.add('', plot_dicts)
    chart.render_to_file('bar_descriptions.svg')
    
    
