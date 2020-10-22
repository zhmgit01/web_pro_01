# -*- coding:utf-8 -*-
# @FileName  :user_page.py
# @Time      :2020/10/22 10:16
# @Author    :zhm
import time

from locator.user_locator import UserLocator
from pages.base_page import BasePage


class UserPage(BasePage):
    """用户页面"""

    def get_user_amount(self):
        """获取投资用户的余额"""
        time.sleep(10)
        self.wait_visibility_ele(UserLocator.user_amount_loc, loc_desc='用户页面_用户余额')
        amount = self.get_element_text(UserLocator.user_amount_loc, loc_desc='用户页面_用户余额')
        amount = amount[:-1]
        return amount
