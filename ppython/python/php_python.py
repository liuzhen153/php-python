#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import socket
import os
import process
import logger

# -------------------------------------------------
# 基本配置
# -------------------------------------------------
LISTEN_PORT = 21230  # 服务侦听端口
CHARSET = "utf-8"  # 设置字符集（和PHP交互的字符集）

# -------------------------------------------------
# 主程序
#    请不要随意修改下面的代码
# -------------------------------------------------
if __name__ == '__main__':

    logger.loginfo("-------------------------------------------")
    logger.loginfo("- PPython Service")
    logger.loginfo("- Time: %s" %
                   time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    logger.loginfo("-------------------------------------------")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP
    sock.bind(('', LISTEN_PORT))
    sock.listen(5)

    logger.loginfo("Listen port: %d" % LISTEN_PORT)
    logger.loginfo("charset: %s" % CHARSET)
    logger.loginfo("Server startup...")

    while 1:
        connection, address = sock.accept()  # 收到一个请求

        # logger.loginfo ("client's IP:%s, PORT:%d" % address)

        # 处理线程
        try:
            process.ProcessThread(connection).start()
        except:
            pass
