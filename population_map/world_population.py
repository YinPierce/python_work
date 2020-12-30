#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import pygal.maps.world as WMap
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle as LCS

from country_codes import get_country_code

#将json文件加载到列表中
filename = "population_data.json"
with open(filename) as fobj:
    pop_data = json.load(fobj)

#绘制每个国家2010人口数的世界地图
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        country_code = get_country_code(country_name)
        if country_code:
            cc_populations[country_code] = population

#根据人口数量，对国家进行分组:少于1000w,1000w~10亿,10亿以上
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for code, pops in cc_populations.items():
    if pops < 10000000:
        cc_pops_1[code] = pops
    elif pops < 1000000000:
        cc_pops_2[code] = pops
    else:
        cc_pops_3[code] = pops

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

#制定地图使用同一个颜色基调，我们选择一个style
wm_style = RotateStyle('#336699', base_style=LCS) #16进制的RGB颜色，前两位表示red,中间两位绿，最后两位表示蓝

wm = WMap.World(style=wm_style)
wm.title = 'World Population in 2010, by country'
wm.add('10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')