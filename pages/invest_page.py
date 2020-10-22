# -*- coding:utf-8 -*-
# @FileName  :invest_page.py
# @Time      :2020/10/22 9:46
# @Author    :zhm
import time

from locator.invest_locator import InvestLocator
from selenium.webdriver.remote.webdriver import WebDriver


class InvestPage:
    """投资页面"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_invest_amount(self, amount):
        """
        输入投资金额
        :param amount: 投资金额
        :return:
        """
        ele = self.driver.find_element(*InvestLocator.invest_input_loc)
        ele.clear()
        ele.send_keys(amount)

    def click_invest(self):
        """点击投资按钮"""
        self.driver.find_element(*InvestLocator.invest_btn_loc).click()

    def get_invest_btn_error_info(self):
        """获取投资按钮上的提示信息"""
        return self.driver.find_element(*InvestLocator.invest_btn_loc).text

    def get_window_error_info(self):
        """获取页面上的错误提示窗口中的内容"""
        time.sleep(2)
        text = self.driver.find_element(*InvestLocator.error_window_loc).text
        return text

    def get_window_success_info(self):
        """获取窗口中的成功的提示信息"""
        time.sleep(2)
        return self.driver.find_element(*InvestLocator.success_window_loc).text

    def get_invest_input_amount(self):
        """获取投资输入框中的余额"""
        ele = self.driver.find_element(*InvestLocator.invest_input_loc)
        # 获取元素的 data-amount 属性
        amount = ele.get_attribute('data-amount')
        return amount

    def click_window_active(self):
        """点击投资成功窗口中的查看并激活"""
        self.driver.find_element(*InvestLocator.success_active_loc).click()

    def click_close_error_window(self):
        """关闭错误窗口"""
        self.driver.find_element(*InvestLocator.error_window_close_loc).click()
