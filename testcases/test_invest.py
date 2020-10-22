# -*- coding:utf-8 -*-
# @FileName  :test_invest.py
# @Time      :2020/10/22 9:17
# @Author    :zhm
"""
测试投资功能：

前置步骤：
    1、打开浏览器
    2、访问登录页面，进行登录
    3、首页点击项目抢投标

投资的用例执行步骤：
    1、输入投资金额
    2、点击投资
        情况一：输入的金额不是10的整数倍，无法进行点击（点击按钮上有对应的提示信息）
            获取按钮上提示的实际结果
        情况二：输入的数据（是10的整数倍或者数据为空等情况）不符合规范，弹框提示对应的错误
            获取弹框中的错误提示
        情况三：投资成功，弹框提示投资成功的信息
            1、获取弹框中投资成功的提示，进行校验
            2、校验用户投资前后的余额
                投资前的余额，可以直接从输入框的data-amount属性中获取
                投资后的余额，投资成功的提示框中有一个点击查看并激活，点击会进入用户页面，用户页面可以获取用户投资之后的余额

后置操作：
    关闭driver



-------------用例执行过程中涉及到的页面和操作------------------
一、登录页面
    1、登录操作  ---OK

二、首页
    1、点击抢投标

三、投资页面
    1、输入投资金额
    2、点击投标
    3、获取点击按钮上的提示
    4、获取页面上的错误弹窗提示内容
    5、获取页面上投资成功的弹框信息
    6、获取输入框的data-amount属性中的用户余额
    7、点击查看并激活

四、用户页面
    1、获取用户余额
"""

import pytest
from casedatas.invest_data import InvestData


class TestInvest:
    """测试投资用例类"""

    @pytest.mark.parametrize('case', InvestData.error_data)
    def test_invest_error_info_btn(self, case, invest_fixture):
        invest_page = invest_fixture[0]
        # 1、输入投资金额
        invest_page.input_invest_amount(case['money'])
        # 2、获取投资按钮中的提示
        res = invest_page.get_invest_btn_error_info()
        expected = case['expected']
        # 3、断言
        assert res == expected

    @pytest.mark.parametrize('case', InvestData.error_popup_data)
    def test_invest_error_window_info(self, case, invest_fixture):
        invest_page = invest_fixture[0]
        # 1、输入投资金额，点击投资
        invest_page.input_invest_amount(case['money'])
        invest_page.click_invest()
        # 2、获取页面弹框中的错误提示
        res = invest_page.get_window_error_info()
        invest_page.click_close_error_window()
        # 3、断言
        expected = case['expected']
        assert res == expected

    # def test_invest_success(self, invest_fixture):
    #     invest_page = invest_fixture
    #     # 1、输入投资金额,点击投资
    #     invest_page.input_invest_amount(100)
    #     invest_page.click_invest()
    #     # 2、获取页面时投资成功的提示
    #     res = invest_page.get_window_success_info()
    #     # 3、断言
    #     expected = '投标成功！'
    #     assert expected == res

    @pytest.mark.parametrize('case', InvestData.success_data)
    def test_invest_success(self, case, invest_fixture):
        invest_page, user_page = invest_fixture
        # 1、获取投资前用户的余额
        start_amount = invest_page.get_invest_input_amount()
        # 2、输入投资金额
        invest_page.input_invest_amount(case['money'])
        # 点击投资
        invest_page.click_invest()
        # 3、获取页面时投资成功的提示
        res = invest_page.get_window_success_info()
        # 4、断言
        expected = case['expected']
        assert res == expected
        # 5、点击查看并激活
        invest_page.click_window_active()
        # 6、用户页面获取用户余额
        end_amount = user_page.get_user_amount()
        # 7、计算投资前后用户余额的变化，并断言
        res_change_amount = float(start_amount) - float(end_amount)
        assert res_change_amount == case['money']
