#!/bin/sh
# 启动或重启ppython服务
ACT=$1 # start restart | stop
ps -ef|grep 'php_python' |grep -v 'grep'| awk '{print $2}'|xargs kill -9
if [[ ${ACT} != 'stop' ]]; then
	project_path=$(cd `dirname $0`; pwd)
	project_name="${project_path%/*}/ppython/python/php_python.py"
	python3 ${project_name} &
fi
echo 'done!'
