# -*- coding:utf-8 -*-
# @FileName  :user_page.py
# @Time      :2020/10/22 10:16
# @Author    :zhm

from selenium.webdriver.remote.webdriver import WebDriver
from locator.user_locator import UserLocator


class UserPage:
    """用户页面"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_amount(self):
        """获取投资用户的余额"""
        amount = self.driver.find_element(*UserLocator.user_amount_loc).text
        amount = amount[:-1]
        return amount
