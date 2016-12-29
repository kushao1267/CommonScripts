# coding=utf-8
import requests
from lxml import etree
from subprocess import Popen
import json
import sys

vpn_url = 'http://www.ishadowsocks.org/'

# config
config = {
    "server": 'server',
    "server_port": 'server_port',
    "local_address": '127.0.0.1',
    "local_port": '1080',
    "password": 'password',
    "timeout": 500,
    "method": 'method',
    "fast_open": False
}

point = {
    '0': {  # 
        'server': "", # server host
        'server_port': , # server port
        'password': "", # password
        'method': "rc4-md5" # mathod
    },
    '1': {  # iss A
        'server': '//*[@id="free"]/div/div[2]/div[1]/h4[1]',
        'server_port': '//*[@id="free"]/div/div[2]/div[1]/h4[2]',
        'password': '//*[@id="free"]/div/div[2]/div[1]/h4[3]',
        'method': '//*[@id="free"]/div/div[2]/div[1]/h4[4]'
    },
    '2': {  # iss B
        'server': '//*[@id="free"]/div/div[2]/div[2]/h4[1]',
        'server_port': '//*[@id="free"]/div/div[2]/div[2]/h4[2]',
        'password': '//*[@id="free"]/div/div[2]/div[2]/h4[3]',
        'method': '//*[@id="free"]/div/div[2]/div[2]/h4[4]'
    },
    '3': {  # iss C
        'server': '//*[@id="free"]/div/div[2]/div[3]/h4[1]',
        'server_port': '//*[@id="free"]/div/div[2]/div[3]/h4[2]',
        'password': '//*[@id="free"]/div/div[2]/div[3]/h4[3]',
        'method': '//*[@id="free"]/div/div[2]/div[3]/h4[4]'
    }
}


def select_point(iss, res):
    server = etree.HTML(res.content).xpath(
        point[iss]['server'])[0].text.split(':')[1] \
        if iss not in ['0'] else point[iss]['server']
    server_port = etree.HTML(res.content).xpath(
        point[iss]['server_port'])[0].text.split(':')[1] \
        if iss not in ['0'] else point[iss]['server_port']
    password = etree.HTML(res.content).xpath(
        point[iss]['password'])[0].text.split(':')[1] \
        if iss not in ['0'] else point[iss]['password']
    method = etree.HTML(res.content).xpath(
        point[iss]['method'])[0].text.split(':')[1] \
        if iss not in ['0'] else point[iss]['method']
    return (server, server_port, password, method)


def main():
    '''
            免费翻墙
    '''
    iss = sys.argv[1]
    file = sys.argv[2]
    res = requests.get(vpn_url)
    # 选择节点,配置ss客户端
    config['server'], config['server_port'], config[
        'password'], config['method'] = select_point(iss, res)
    # 改变配置
    try:
        with open(file, 'w') as f:
            json.dump(config, f)
            # 运行配置脚本
            Popen('sudo sslocal -c ' + file, shell=True)
    except Exception:
        print('打开文件失败！')
    finally:
        exit(0)


if __name__ == '__main__':
    main()
