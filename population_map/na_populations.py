#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

import pygal.maps.world as WMap

wm = WMap.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')