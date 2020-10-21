# -*- coding:utf-8 -*-
# @FileName  :index_locator.py
# @Time      :2020/10/21 11:01
# @Author    :zhm

from selenium.webdriver.common.by import By


class IndexLocator:
    """首页元素定位"""
    # 我的帐户
    user_info_loc = (By.XPATH, '//a[contains(text(),"我的帐户")]')
    # 退出按钮
    quit_login_loc = (By.XPATH, '//a[contains(text(),"退出")]')
