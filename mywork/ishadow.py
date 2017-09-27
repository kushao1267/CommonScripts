# coding=utf-8
import os
import json
import requests

from lxml import etree
"""
定时交给shell脚本
"""

BASE_URL = 'https://ss.ishadowx.net/'
HEAD_PAGE = BASE_URL + 'index_cn.html'
CONFIG_GLOABL = ''
DIR_NAME = os.path.dirname(os.path.abspath(__file__))


def _get_ss_config(url):
    """
    抓取ss配置
    """
    res = requests.get(url)
    tree = etree.HTML(res.content)
    server_host = tree.xpath(r'//*[@id="ipsgc"]/text()')[0]
    server_port = int(tree.xpath(
        r'//*[@id="portfolio"]/div[2]/div[2]/div/div[9]/div/div/div/h4[2]/text()')[0].split('：')[-1])
    password = tree.xpath(r'//*[@id="pwsgc"]/text()')[0]
    method = tree.xpath(
        r'//*[@id="portfolio"]/div[2]/div[2]/div/div[9]/div/div/div/h4[4]/text()')[0].split(':')[-1]
    qrcode = '{0}{1}'.format(BASE_URL, tree.xpath(
        r'//*[@id="portfolio"]/div[2]/div[2]/div/div[9]/div/div/div/h4[5]/a/text()'))
    local_host = "127.0.0.1"
    local_port = 1080
    ss_config = {
        'server': server_host,
        'server_port': server_port,
        'local_adress': local_host,
        'local_port': local_port,
        'method': method,
        'password': password,
        'fast_open': False,
        'timeout': 400
    }
    ss_config = json.dumps(ss_config)
    with open('{}/ss_log'.format(DIR_NAME), 'a') as l:
        l.write('{} {}\n'.format('获取配置成功:'.encode('utf8'),ss_config))
    return ss_config


def save_config(config):
    """
    保存配置文件
    """
    try:
        with open('{}/ss_config.json'.format(DIR_NAME), 'w') as f:
            f.write(config)
    except Exception as e:
        with open('{}/ss_log'.format(DIR_NAME), 'a') as l:
            l.write(u'{} {}\n'.format('创建配置文件失败:'.encode('utf8'), e))


if __name__ == '__main__':
    ss_config = _get_ss_config(HEAD_PAGE)
    save_config(ss_config)
