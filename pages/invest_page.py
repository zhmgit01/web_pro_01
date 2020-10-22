# -*- coding:utf-8 -*-
# @FileName  :invest_page.py
# @Time      :2020/10/22 9:46
# @Author    :zhm

from locator.invest_locator import InvestLocator
from pages.base_page import BasePage


class InvestPage(BasePage):
    """投资页面"""

    def input_invest_amount(self, amount):
        """
        输入投资金额
        :param amount: 投资金额
        :return:
        """
        ele = self.get_element(InvestLocator.invest_input_loc, loc_desc='投资页面_输入投资金额')
        ele.clear()
        ele.send_keys(amount)

    def click_invest(self):
        """点击投资按钮"""
        self.click_element(InvestLocator.invest_btn_loc, loc_desc='投资页面_投资按钮')

    def get_invest_btn_error_info(self):
        """获取投资按钮上的提示信息"""
        return self.get_element_text(InvestLocator.invest_btn_loc, loc_desc='投资页面_投资按钮')

    def get_window_error_info(self):
        """获取页面上的错误提示窗口中的内容"""
        # time.sleep(2)
        self.wait_visibility_ele(InvestLocator.error_window_loc, loc_desc='投资页面_错误弹框提示')
        text = self.get_element_text(InvestLocator.error_window_loc, loc_desc='投资页面_错误弹框提示')
        return text

    def get_window_success_info(self):
        """获取窗口中的成功的提示信息"""
        # time.sleep(2)
        self.wait_visibility_ele(InvestLocator.success_window_loc, loc_desc='投资页面_投资成功弹框')
        return self.get_element_text(InvestLocator.success_window_loc, loc_desc='投资页面_投资成功弹框')

    def get_invest_input_amount(self):
        """获取投资输入框中的余额"""
        return self.get_element_attr(InvestLocator.invest_input_loc, attr='data-amount', loc_desc='投资页面_投资输入框中的余额')

    def click_window_active(self):
        """点击投资成功窗口中的查看并激活"""
        self.click_element(InvestLocator.success_active_loc, loc_desc='投资页面_成功窗口的查看并激活')

    def click_close_error_window(self):
        """关闭错误窗口"""
        self.click_element(InvestLocator.error_window_close_loc, loc_desc='投资页面_关闭错误窗口')
