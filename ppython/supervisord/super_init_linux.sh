#!/bin/sh
# $1为IP地址
#变量设置
echo '该脚本不完善，请自行测试！！！！'
pip2 install supervisor
project_path=$(cd `dirname $0`; pwd)
ppython_path="${project_path%/*}/"
python_path="${ppython_path}/python/"
super_path="${ppython_path}/supervisord/"
ppython_sh="${ppython_path}/ppython.sh"
ipaddr='172.0.0.1'
if [ ! $1 ]; then
  local_ip=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}')
else
  local_ip=$1
fi

echo '开始修改配置文件'

CON3="directory=${python_path} ; 命令执行目录"
CON5="stdout_logfile=${ppython_path}/log/ppython.log"
CON6="stderr_logfile=${ppython_path}/log/ppython_error.log"
FILE="${super_path}/ppython.ini"
sed -i "3c${CON3}" $FILE
sed -i "5c${CON5}" $FILE
sed -i "6c${CON6}" $FILE

CON23="port=${local_ip}:8886        ; ip_address:port specifier, *:port for all iface"
FILE2="${super_path}/supervisord.conf"
sed -i "23c${CON23}" $FILE2
