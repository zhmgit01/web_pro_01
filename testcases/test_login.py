# -*- coding:utf-8 -*-
# @FileName  :test_login.py
# @Time      :2020/10/21 11:17
# @Author    :zhm

import pytest
from casedatas.login_data import LoginData
from common.handle_log import log


class TestLogin:
    """登录的测试用例类"""

    # 参数化登录数据
    @pytest.mark.parametrize('case', LoginData.login_data_is_none)
    def test_login_data_is_none(self, case, login_setup):
        login_page, index_page = login_setup
        login_page.open_login_page()

        # 1、登录
        login_page.login(case['phone'], case['pwd'])
        # 2、获取页面上的错误提示
        res = login_page.get_page_error_info()
        # 3、断言是否登录成功
        try:
            assert case['expected'] == res
        except AssertionError as e:
            log.error('用例---{}---执行失败'.format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例---{}---执行失败'.format(case['title']))

    @pytest.mark.parametrize('case', LoginData.login_toast_error_data)
    def test_login_toast_error(self, case, login_setup):
        login_page, index_page = login_setup
        login_page.open_login_page()

        # 1、登录
        login_page.login(case['phone'], case['pwd'])
        # 2、获取toast弹窗中的错误提示
        res = login_page.get_toast_error_info()
        # 3、断言是否登录成功
        try:
            assert case['expected'] == res
        except AssertionError as e:
            log.error('用例---{}---执行失败'.format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例---{}---执行失败'.format(case['title']))

    @pytest.mark.parametrize('case', LoginData.login_pass_data)
    def test_login_pass(self, case, login_setup):
        login_page, index_page = login_setup
        login_page.open_login_page()

        # 1、登录
        login_page.login(case['phone'], case['pwd'])
        # 2、获取首页中登录后的帐户信息
        res = index_page.is_login()
        # 3、断言
        try:
            assert res
        except AssertionError as e:
            log.error('用例---{}---执行失败'.format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例---{}---执行失败'.format(case['title']))
            # 登录成功之后，点击退出
            index_page.click_quit_login()
