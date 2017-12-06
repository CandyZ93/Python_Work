#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  python_repos.py
 


if __name__ == '__main__':
    import requests
    import pygal
    from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
    
    #执行API调用并存储响应
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    print("Status Code:", r.status_code)
    
    #将API响应存储在一个变量中
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])
    
    #探索有关仓库的信息
    repo_dicts = response_dict['items']
    print("Repositories returned:", len(repo_dicts))
    
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        
        plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']), #此处报错，尝试强制转换为字符串
        'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)
        
    #~ #默认工具提示--项目名
    #~ names, stars = [], []
    #~ for repo_dict in repo_dicts:
        #~ names.append(repo_dict['name'])
        #~ stars.append(repo_dict['stargazers_count'])
        
    # 可视化
    my_style = LS('#333366', base_style=LCS)
    
    #创建Pygal类的Config实例
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    
    chart = pygal.Bar(my_config, style=my_style)
    #~ chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Most-Starred Python Projects on Github'
    chart.x_labels = names
    
    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')
        
    #~ #输出所有排名靠前的项目的详细信息
    #~ print("\nSelected information about each repository:")
    #~ for repo_dict in repo_dicts:
        #~ print('\nName:', repo_dict['name'])
        #~ print('Owner:', repo_dict['owner']['login'])
        #~ print('Stars:', repo_dict['stargazers_count'])
        #~ print('Repository:', repo_dict['html_url'])
        #~ print('Description:', repo_dict['description'])
        
    
    #~ #研究第一个仓库
    #~ repo_dict = repo_dicts[0]
    #~ print("\nKeys:", len(repo_dict))
    #~ for key in sorted(repo_dict.keys()):
        #~ print(key)
        
    #~ print("\nSelected information about first repository:")
    #~ print('Name:', repo_dict['name'])
    #~ print('Owner:', repo_dict['owner']['login'])
    #~ print('Stars:', repo_dict['stargazers_count'])
    #~ print('Repository:', repo_dict['html_url'])
    #~ print('Created:', repo_dict['created_at'])
    #~ print('Update:', repo_dict['updated_at'])
    #~ print('Description:', repo_dict['description'])
    
    
    
    #~ #处理结果
    #~ print(response_dict.keys())
