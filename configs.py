#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 13:42
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# config配置部分

LOGIN_URL = 'http://betawx.touzijiajia.com'

#谷歌手机模式配置
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

# 账号信息
USER = {
    'user': {
        '账号': '18665927085',
        '密码': 'zhuzhu123'
    },
    'admin': {
        '账号': 'xx',
        '密码': 'xx'
    }
}