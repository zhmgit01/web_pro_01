# -*- coding:utf-8 -*-
# @FileName  :index_page.py
# @Time      :2020/10/21 11:08
# @Author    :zhm

from locator.index_locator import IndexLocator


class IndexPage(object):
    """首页"""

    def __init__(self, driver):
        self.driver = driver

    def is_login(self):
        """判断用户是否登录"""
        try:
            self.driver.find_element(*IndexLocator.user_info_loc)
        except:
            return False
        else:
            return True

    def click_quit_login(self):
        """点击退出登录"""
        self.driver.find_element(*IndexLocator.quit_login_loc).click()

    def click_invest(self):
        """点击抢投标"""
        self.driver.find_element(*IndexLocator.invest_loc).click()
