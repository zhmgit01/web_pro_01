# -*- coding:utf-8 -*-
# @FileName  :login_page.py
# @Time      :2020/10/21 10:13
# @Author    :zhm

from common.handle_config import conf
from locator.login_locator import LoginLocator
from pages.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""

    def login(self, mobile_phone, pwd):
        """
        登录
        :param mobile_phone: 手机号
        :param pwd: 密码
        :return:
        """
        # 1、输入账号
        self.input_send_keys(LoginLocator.input_mobile_locator, mobile_phone, loc_desc='登录页面_输入手机号')
        # 2、输入密码
        self.input_send_keys(LoginLocator.input_pwd_locator, pwd, loc_desc='登录页面_输入密码')
        # 3、点击登录
        self.click_element(LoginLocator.login_btn_locator)

    def get_page_error_info(self):
        """获取页面上的错误提示"""
        res = self.get_element_text(LoginLocator.page_error_locator,loc_desc='登录页面_错误信息提示')
        return res

    def get_toast_error_info(self):
        """获取toast弹窗错误提示"""
        self.wait_visibility_ele(LoginLocator.toast_error_info_locator,loc_desc='登录页面_toast错误弹框')
        return self.get_element_text(LoginLocator.toast_error_info_locator)

    def open_login_page(self):
        """打开登录页面"""
        self.driver.get(conf.get('env', 'base_url') + conf.get('url_path', 'login'))
