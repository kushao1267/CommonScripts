#!/bin/bash
# 用于查看指定端口是否占用，并可选择性杀死占用端口的进程
# 目前可强制杀死指定名称的进程，忽略大小写匹配

if [ ! -n "$1" ]; then
    sudo lsof -nP -iTCP -sTCP:LISTEN
else
    sudo lsof -nP -iTCP -sTCP:LISTEN | grep -i $1
    echo "============================================"
    read -p "unbound this port ? (y/n)
============================================
" choose
    if [ "$choose" = "y" ] || [ "$choose" = "Y" ]; then
        sudo lsof -nP -iTCP -sTCP:LISTEN | grep -i -m 1 $1 | awk '{print $2;}' | xargs kill -9
    fi
fi
