# -*- coding:utf-8 -*-
# @FileName  :login_data.py
# @Time      :2020/10/21 11:16
# @Author    :zhm


class LoginData:
    """登录功能用例测试数据"""
    login_pass_data = [
        {"title": "登录成功", "phone": "18684720553", "pwd": "python"}
    ]

    login_data_is_none = [
        {"title": "密码为空", "phone": "18684720553", "pwd": "", "expected": "请输入密码"},
        {"title": "手机号为空", "phone": "", "pwd": "python", "expected": "请输入手机号"},
    ]

    login_toast_error_data = [
        {"title": "帐号或密码错误", "phone": "18684720553", "pwd": "123", "expected": "帐号或密码错误!"},
    ]
