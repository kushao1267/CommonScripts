# -*- coding: utf-8 -*-
import requests
from subprocess import Popen
import os

PROXY = {'http': "socks5://127.0.0.1:1080"}  # 配置本地代理端口
TIMEOUT = 4
URL_CHECK = 'http://www.google.com'  # 用于检测ss是否连接成功
CONFIG_NAME = 'ss_free'  # ss的配置文件名,可自定义
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def main():
    '''
        自动检测是否翻墙，清除后台，重新选择节点。
    '''
    print('-' * 43)
    try:
        gen_config(CONFIG_NAME)
        key = check()
        if key in ['Y', 'y']:
            switch()
    except:
        print('未连接VPN...')
        switch()
    finally:
        exit(0)
        print('-' * 43)


def gen_config(file_name):
    '''
        生成ss的config文件,并修改权限
    '''
    try:
        global FILE
        FILE = '/etc/' + file_name + '.json'
        cmd = 'sudo chmod 777 ' + \
            FILE if os.path.exists(FILE) else 'sudo touch ' + \
            FILE + ' ; sudo chmod 777 ' + FILE
        Popen(cmd, shell=True)
    except:
        print('请使用超级权限!')
        exit(0)


def check():
    '''
        检查节点是否可用
    '''
    proxies = PROXY  # 安装pysocks使requests能够代理
    res = requests.get(URL_CHECK,
                       proxies=proxies, timeout=TIMEOUT)
    print('VPN已连接 :{} !'.format(res.status_code))
    key = input('是否切换VPN？ y/Y')
    return key


def switch():
    '''
        重启翻墙程序.
        防止上次后台运行时的进程占用端口.
    '''
    kill_process('sslocal')
    iss = input('选择节点?  (0,1,2,3)?')
    if iss not in ['0', '1', '2', '3']:
        iss = '0'
    task = 'sudo nohup python3 ' + BASE_PATH + '/' + '{0} {1} {2} & '.format(
        'ssconfig.py', iss, FILE)
    print(task)
    Popen(task, shell=True)
    print('连接成功...')


def kill_process(pid_name):
    '''
        kill指定名称的进程
    '''
    Popen("sudo pkill -f {0}".format(pid_name), shell=True)
    print('清除进程...')


if __name__ == '__main__':
    main()
