# -*- encoding=utf8 -*-
__author__ = "lvxinjin"

from airtest.core.api import *

auto_setup(__file__)
tonghuashun = "com.hexin.plat.android"
d = device()
all_app = d.list_app()
print(all_app)
stop_app(tonghuashun)
if tonghuashun in all_app:
    start_app(tonghuashun)