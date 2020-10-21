# -*- coding:utf-8 -*-
# @FileName  :handle_log.py
# @Time      :2020/10/21 9:43
# @Author    :zhm

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.handle_config import conf
from common.handle_path import LOG_DIR


def create_logger():
    """创建日志收集器"""

    # 1、创建收集器
    log = logging.getLogger('test')
    # 设置收集器日志的等级
    log.setLevel(conf.get('logging', 'level'))

    # 2、创建输出到文件的输出渠道（按时间轮转）
    fh = TimedRotatingFileHandler(filename=os.path.join(LOG_DIR, conf.get('logging', 'log_name')),
                                  when='d',
                                  interval=1,
                                  backupCount=7,
                                  encoding='utf-8')
    # 设置输出等级
    fh.setLevel(conf.get('logging', 'fh_level'))
    # 添加到收集器中
    log.addHandler(fh)

    # 3、创建输出到控制台的输出渠道
    sh = logging.StreamHandler()
    # 设置输出等级
    sh.setLevel(conf.get('logging', 'sh_level'))
    # 添加到收集器中
    log.addHandler(sh)

    # 4、设置日志输出格式
    formatter = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    mate = logging.Formatter(formatter)
    fh.setFormatter(mate)
    sh.setFormatter(mate)

    return log


log = create_logger()
