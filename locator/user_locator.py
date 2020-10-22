# -*- coding:utf-8 -*-
# @FileName  :user_locator.py
# @Time      :2020/10/22 10:16
# @Author    :zhm

from selenium.webdriver.common.by import By


class UserLocator:
    """用户页面元素"""

    # 用户余额
    user_amount_loc = (By.XPATH, '//li[@class="color_sub"]')
