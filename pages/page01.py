#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-04-17 13:17
#   页面元素位置信息
login={
    'name': '微投帮登陆页',
    'url': '/#/login',
    '密码登陆选择按钮': ['xpath', "//span[contains(text(),'密码登录')]"],
    '用户名输入框': ['xpath', 'html/body/div/div/div/div[3]/div[1]/input'],
    '密码输入框': ['xpath', "html/body/div/div/div/div[3]/div[3]/input"],
    '登陆按钮': ['xpath', "//div[contains(text(),'登录')]"],
}

sy={
    'name': '微投帮首页',
    'url': '/#/home',
    '首页菜单按钮': ['xpath', "//div[contains(text(),'首页')]"],
    '我的菜单按钮': ['xpath', "//div[contains(text(),'我的')]"],
    '首页搜索框': ['xpath', "//div[@id='Home']/div[1]/div[1]/a/div/input"],
    '顶部搜索框': ['xpath', "//div[@id='Search']/div[1]/div/form/input"],
    '顶部搜索按钮': ['xpath', "//div[@id='Search']/div[1]/div/form/i"],
    '搜索结果第一列标题': ['xpath', "//p[contains(text(),'足协背书 动量科技欲融资3000万')]"],
    '行业标签': ['xpath', "//span[contains(text(),'行业标签')]"],
    '人工智能': ['xpath', "html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/ul[1]/li[2]"],
    '大数据': ['xpath', "html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/ul[1]/li[3]"],
    '标签确定按钮': ['xpath', "//div[contains(text(),'确定')]"],
    '所在城市': ['xpath', "//span[contains(text(),'所在城市')]"],
    '北京': ['xpath', "html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/ul[2]/li[2]"],
    '上海': ['xpath', "html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/ul[2]/li[3]"],
    '融资轮次': ['xpath', "//span[contains(text(),'融资轮次')]"],
    '天使轮': ['xpath', "html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/ul[3]/li[2]"],
    'Pre-A轮': ['xpath', "html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/ul[3]/li[3]"],
    '项目列表项目标题':['xpath',"html/body/div/div/div[3]/div[1]/ul/div/div[1]/div[1]/p[1]"]
}

xqy={
    'name': '项目详情页',
    'url': '/#/projectDetail?id=285',
    '项目详情页项目标题': ['xpath', "//div[@id='ProjectDetail']/div[3]/div[1]/div/h2/span[1]"],
    '查看BP按钮': ['xpath', "html/body/div/div/div[8]/div[1]/p"],
}