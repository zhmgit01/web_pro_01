# -*- coding:utf-8 -*-
# @FileName  :handle_path.py
# @Time      :2020/10/21 9:32
# @Author    :zhm

import os

# 项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例的目录路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')

# 测试报告的目录路径
REPORT_DIR = os.path.join(BASE_DIR, 'test_results/reports')

# 日志目录的项目路径
LOG_DIR = os.path.join(BASE_DIR, 'test_results/logs')

# 错误截图存放的目录路径
ERROR_DIR = os.path.join(BASE_DIR, 'test_results/error_images')

# 用例数据的项目路径
DATA_DIR = os.path.join(BASE_DIR, 'casedatas')

# 配置文件目录路径
CONF_DIR = os.path.join(BASE_DIR, 'config')

if __name__ == '__main__':
    print(CONF_DIR)
