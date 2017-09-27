#!/bin/zsh

home=/Users/jianliu
echo "active the python3 environment..."
source $home/py3.5/bin/activate
ss_abs=$(which sslocal)
work_dir=$(cd `dirname $0`; pwd)
echo "grap the shadowsocks configurations..."
python $work_dir/ishadow.py 
echo "restart the sslocal service"
$ss_abs -c $work_dir/ss_config.json -d restart
