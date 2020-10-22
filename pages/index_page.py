# -*- coding:utf-8 -*-
# @FileName  :index_page.py
# @Time      :2020/10/21 11:08
# @Author    :zhm

from locator.index_locator import IndexLocator
from pages.base_page import BasePage


class IndexPage(BasePage):
    """首页"""

    def is_login(self):
        """判断用户是否登录"""
        try:
            self.get_element(IndexLocator.user_info_loc, loc_desc='首页_我的帐户')
        except:
            return False
        else:
            return True

    def click_quit_login(self):
        """点击退出登录"""
        self.click_element(IndexLocator.quit_login_loc, loc_desc='首页_退出登录')

    def click_invest(self):
        """点击抢投标"""
        self.click_element(IndexLocator.invest_loc, loc_desc='首页_抢投标')
