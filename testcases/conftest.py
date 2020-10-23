# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2020/10/21 11:23
# @Author    :zhm

import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from pages.user_page import UserPage
from pages.invest_page import InvestPage
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from common.handle_config import conf


def create_driver():
    """打开浏览器，创建driver对象"""
    # 读取配置文件中的配置，判断是否以无头模式运行
    if conf.getboolean('run', 'headless'):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        driver = Chrome()
    return driver


@pytest.fixture(scope='class')
def login_setup():
    """前置方法 登录"""
    driver = create_driver()
    driver.implicitly_wait(10)
    driver.get(conf.get('env', 'base_url') + conf.get('url_path', 'login'))
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    # 登录的后置 退出driver
    driver.quit()


@pytest.fixture(scope='class')
def invest_fixture():
    """投资用例的前置条件"""
    driver = create_driver()
    # 最大化窗口
    driver.maximize_window()
    # 设置隐式等待
    driver.implicitly_wait(15)
    # 实例登录页面对象
    login_page = LoginPage(driver)
    # 打开登录页面
    login_page.open_login_page()
    # 进行登录
    login_page.login(mobile_phone=conf.get('test_data', 'mobile'), pwd=conf.get('test_data', 'pwd'))
    # 实例首页对象
    index_page = IndexPage(driver)
    # 首页点击投资
    index_page.click_invest()
    # 实例投资页面对象
    invest_page = InvestPage(driver)
    # 实例用户页面对象
    user_page = UserPage(driver)

    yield invest_page, user_page
    driver.quit()
