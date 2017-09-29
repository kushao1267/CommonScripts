#!/bin/zsh

home=/Users/jianliu

echo "active the python3 environment..."
source $home/py3.5/bin/activate
ss_abs=$(which sslocal)
work_dir=$(cd `dirname $0`; pwd)

echo "grap the shadowsocks configurations..."
if [ -z $1 ];then
    python $work_dir/ishadow-new.py URL
    echo "Didn't input an argument,using default settings..."
else
    python $work_dir/ishadow-new.py $1
    echo "using $1 method to set shadowsocks.."
fi

echo "restart the sslocal service..."
$ss_abs -c $work_dir/ss_config.json -d restart

exit 0
