#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import sys
from datetime import datetime
from pytz import timezone

cst_tz = timezone('Asia/Shanghai')  # 时区设置


def loginfo(*args, **kwargs):
    '''打印日志
    :param args:string
    :param kwargs:dict | 可自主拓展
    '''
    more_msg = ''
    if 'params' in kwargs.keys():
        params = kwargs['params']
        # 这里是自主拓展用

    now = datetime.now().replace(tzinfo=cst_tz)
    # 获取上级目录下的log
    log_dir = os.path.dirname(os.path.dirname(
        __file__)) + '/log/' + now.strftime('%Y%m%d')
    check_dir(log_dir)
    log_file = log_dir + '/' + now.strftime('%H') + '.log'
    # 获取调用方信息
    sys_info = sys._getframe()
    try:
        f = open(log_file, 'a')
        for info in args:
            # print(str(info))
            # 如果带上文件信息 + ' [file - ' + sys_info.f_code.co_filename +  ']\r\n'
            f.write('[' + now.strftime('%Y-%m-%d %H:%M:%S') + ' line:' + str(sys_info.f_back.f_lineno) +
                    '] - ' + more_msg + str(info) + ' [func:' + sys_info.f_back.f_code.co_name + ']\r\n')
    finally:
        if f:
            f.close()


def check_dir(base_dir):
    '''检查和生成路径
    :param base_dir:string
    '''
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
