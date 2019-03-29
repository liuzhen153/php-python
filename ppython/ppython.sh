#!/bin/sh
# 启动或重启ppython服务
ACT=$1 # start restart | stop
ps -ef|grep 'php_python' |grep -v 'grep'| awk '{print $2}'|xargs kill -9
if [[ ${ACT} != 'stop' ]]; then
	python3 ./python/php_python.py &
fi