# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2020/10/21 11:23
# @Author    :zhm

import pytest
from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from common.handle_config import conf


@pytest.fixture(scope='class')
def login_setup():
    """前置方法 登录"""
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get(conf.get('env', 'base_url') + conf.get('url_path', 'login'))
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    # 登录的后置 退出driver
    driver.quit()
