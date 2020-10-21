# -*- coding:utf-8 -*-
# @FileName  :handle_config.py
# @Time      :2020/10/21 9:46
# @Author    :zhm

import os
from configparser import ConfigParser
from common.handle_path import CONF_DIR


class Config(ConfigParser):

    def __init__(self, filename, encoding='utf-8'):
        super().__init__()
        self.read(filename, encoding=encoding)
        self.filename = filename
        self.encoding = encoding

    def write_data(self, section, option, value):
        """写入配置文件"""
        self.set(section, option, value)
        self.write(fp=open(self.filename, 'w', encoding=self.encoding))


# 创建配置文件解析器
conf = Config(os.path.join(CONF_DIR, 'config.ini'))
