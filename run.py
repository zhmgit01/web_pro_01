# -*- coding:utf-8 -*-
# @FileName  :run.py
# @Time      :2020/10/21 9:28
# @Author    :zhm

import os
import pytest

# 1、生成alluer测试报告数据
pytest.main(["--alluredir=test_results/reports",  # 指定生产allure报告的路径
             '--reruns', '3',  # 指定失败重运行的次数
             '--reruns-delay', '2'  # 指定失败重运行的间隔时间
             ])

# 2、启动allure服务
# os.system('allure serve test_result/reports')
