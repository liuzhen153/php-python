#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import time
import socket
import process
import logger

# -------------------------------------------------
# 基本配置
# -------------------------------------------------
LISTEN_PORT = 21230  # 服务侦听端口
CHARSET = "utf-8"  # 设置字符集（和PHP交互的字符集）
LISTEN_NUM = 5  # 操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了

# -------------------------------------------------
# 主程序
#    请不要随意修改下面的代码
# -------------------------------------------------
if __name__ == '__main__':
    s = None
    err_msg = ''
    for res in socket.getaddrinfo('', LISTEN_PORT, socket.AF_INET,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            err_msg = msg
            continue
        try:
            s.bind(sa)
            s.listen(LISTEN_NUM)
        except OSError as msg:
            s.close()
            s = None
            err_msg = msg
            continue
        break
    if s is None:
        logger.loginfo('could not open socket:' + str(err_msg))
        sys.exit(1)

    logger.loginfo("-------------------------------------------")
    logger.loginfo("- PPython Service")
    logger.loginfo("- Time: %s" %
                   time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    logger.loginfo("-------------------------------------------")
    logger.loginfo("Listen port: %d" % LISTEN_PORT)
    logger.loginfo("charset: %s" % CHARSET)
    logger.loginfo("Server startup...")

    while True:
        conn, addr = s.accept()
        try:
            process.ProcessThread(conn).start()
        except Exception as e:
            logger.loginfo(str(e))
            pass
