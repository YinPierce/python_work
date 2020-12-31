#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Stats code:", r.status_code)

repository_dict = r.json() #返回一个字典
print('Total repositories: ', repository_dict['total_count'])

#探索仓库信息,'items'键对应了所有github上有关python的项目,它的值是一个列表,元素是字典
repos_list = repository_dict['items']
print('Repositories Returned:', len(repos_list))

#研究第一个仓库
# repo_dict = repos_list[0]
# print('Keys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nSelected information about each repository:")
# for repo_dict in repos_list:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login']) #owner对应的value也是个字典，所以再用键值'login'得到用户名
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

#使用pygal可视化受欢迎的python项目
names, stars_desc_dicts = [], []
for repo_dict in repos_list:
    names.append(repo_dict['name'])
    star_desc_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    if repo_dict['description'] == None:
        star_desc_dict['label'] = ''

    stars_desc_dicts.append(star_desc_dict)

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18 #主标签字体，y轴方向上为 5000 整数倍的刻度
my_config.truncate_label = 15   #将较长的项目名缩短为 15 个字符
my_config.show_y_guides = False #隐藏图表中的水平线
my_config.width = 1200

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) #show_legend=False表示隐藏了图例,左上角可以选择的图标
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars_desc_dicts)
chart.render_to_file('python_repos.svg')