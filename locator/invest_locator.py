# -*- coding:utf-8 -*-
# @FileName  :invest_locator.py
# @Time      :2020/10/22 9:29
# @Author    :zhm

from selenium.webdriver.common.by import By


class InvestLocator:
    """投资页面定位元素"""

    # 投资金额输入框
    invest_input_loc = (By.XPATH, '//div[@class="clearfix left"]//input')
    # 投资按钮
    invest_btn_loc = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 错误提示框
    error_window_loc = (By.XPATH, '//div[@class="text-center"]')
    # 错误窗口的确认
    error_window_close_loc = (By.XPATH, '//a[text()="确认"]')
    # 投标成功窗口
    success_window_loc = (By.XPATH, '//div[text()="投标成功！"]')
    # 查看并激活 元素定位
    success_active_loc = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
