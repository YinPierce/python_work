#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

from pygal_maps_world.i18n import COUNTRIES

#COUNTRIES是一个字典，键是每个国家的两位国家码
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])