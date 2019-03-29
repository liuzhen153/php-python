#!/bin/sh
# 启动或重启supervisor服务
project_path=$(cd `dirname $0`; pwd)
ppython_path="${project_path%/*}/"
super_path="${ppython_path}/supervisord/"
ps -ef|grep 'supervisord.conf' |grep -v 'grep'| awk '{print $2}'|xargs kill -9
ps -ef|grep 'ppython.sh' |grep -v 'grep'| awk '{print $2}'|xargs kill -9
ps -ef|grep 'php_python.py' |grep -v 'grep'| awk '{print $2}'|xargs kill -9
supervisord -c ${super_path}/supervisord.conf
echo 'done'
