# -*- coding:utf-8 -*-
# @FileName  :login_page.py
# @Time      :2020/10/21 10:13
# @Author    :zhm

from common.handle_config import conf
from locator.login_locator import LoginLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(object):
    """登录页面"""

    def __init__(self, driver):
        self.driver = driver

    def login(self, mobile_phone, pwd):
        """
        登录
        :param mobile_phone: 手机号
        :param pwd: 密码
        :return:
        """
        # 1、输入账号
        login_input = self.driver.find_element(*LoginLocator.input_mobile_locator)
        # 清空输入框中缓存内容
        login_input.clear()
        login_input.send_keys(mobile_phone)

        # 2、输入密码
        pwd_input = self.driver.find_element(*LoginLocator.input_pwd_locator)
        pwd_input.clear()
        pwd_input.send_keys(pwd)

        # 3、点击登录
        self.driver.find_element(*LoginLocator.login_btn_locator).click()

    def get_page_error_info(self):
        """获取页面上的错误提示"""
        res = self.driver.find_element(*LoginLocator.page_error_locator).text
        return res

    def get_toast_error_info(self):
        """获取toast弹窗错误提示"""
        WebDriverWait(self.driver, 15, 0.5).until(
            EC.visibility_of_element_located(LoginLocator.toast_error_info_locator)
        )
        res = self.driver.find_element(*LoginLocator.toast_error_info_locator).text
        return res

    def reset_login_page(self):
        """重置登录页面"""
        self.driver.get(conf.get('env', 'base_url') + conf.get('url_path', 'login'))
