#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import logging
import logging.handlers

def loginfo(msg):
    '''打印日志
    :param args:string
    :param kwargs:dict | 可自主拓展
    '''
    # 获取上级目录下的log
    log_dir = os.path.dirname(os.path.dirname(
        __file__)) + '/log/'
    logger = logging.getLogger('ppython')
    logger.setLevel(logging.DEBUG)
    ppython_handler = logging.handlers.TimedRotatingFileHandler(log_dir + '/python/all.log', 'D', 1, 10) # 按天进行分割，日志只保留10天
    ppython_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(ppython_handler)
    logger.info(msg)
    #  添加下面一句，在记录日志之后移除句柄
    logger.removeHandler(ppython_handler)
