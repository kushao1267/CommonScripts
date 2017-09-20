#!/bin/zsh

source /home/jonliu/env3/bin/activate
python /home/jonliu/mywork/ishadow.py
/usr/local/bin/sslocal -c /home/jonliu/mywork/ss_config.json -d restart
