# -*- coding:utf-8 -*-
# @FileName  :login_locator.py
# @Time      :2020/10/21 10:16
# @Author    :zhm

from selenium.webdriver.common.by import By


class LoginLocator:
    """登录页面元素定位"""
    # 手机号输入框
    input_mobile_locator = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    input_pwd_locator = (By.XPATH, '//input[@name="password"]')
    # 点击按钮
    login_btn_locator = (By.XPATH, '//button[text()="登录"]')
    # 登录页面错误提示
    page_error_locator = (By.XPATH, '//div[@class="form-error-info"]')
    # 登录页面toast弹框错误提示
    toast_error_info_locator = (By.XPATH, '//div[@class="layui-layer-content"]')
