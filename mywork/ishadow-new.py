# -*- coding: utf-8 -*-
import os
import sys
import json
import base64
from time import sleep
import requests
from PIL import Image
import zbarlight
from lxml import etree
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


BASE_URL = 'https://ss.ishadowx.net/'
HEAD_PAGE = BASE_URL + 'index_cn.html'
CONFIG_GLOABL = ''
DIR_NAME = os.path.dirname(os.path.abspath(__file__))
TIME_SECONDS = 5
FROM_EMAIL_ADDRESS = '461698053@qq.com'
TO_EMAIL_ADDRESS = 'kushao1267@aliyun.com'
KEY_FROM_QQ = ''


def send_email(qrimg_path):
    from_mail = FROM_EMAIL_ADDRESS
    to_mail = TO_EMAIL_ADDRESS

    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg['Subject'] = 'SS config from ishadow'

    body = 'ishadow config :'
    # 其中cid项从content-id中取出对应的附件,展示在mail内容中
    con = MIMEText(
        '<b> {} </b><img alt="" src="cid:qr_img.png"/>'.format(body), 'html')
    msg.attach(con)

    img = MIMEImage(open(qrimg_path, 'rb').read())
    img.add_header('Content-ID', 'qr_img.png')   # 此项将图片表示content-id
    msg.attach(img)

    server = smtplib.SMTP(host='smtp.qq.com')
    server.starttls()
    try:
        # 从qq邮箱配置获取key
        server.login(FROM_EMAIL_ADDRESS, KEY_FROM_QQ)
    except Exception as e:
        with open('{}/ss_log'.format(DIR_NAME), 'a') as l:
            l.write('发信服务挂了: {}\n'.format(e))
    server.sendmail(from_mail, to_mail, msg.as_string())
    server.quit()


def _qr_decode(img_path):
    with open(img_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
    codes = zbarlight.scan_codes('qrcode', image)
    config_list = tuple(re.split(r'[\'\:\@]', str(
        base64.b64decode(codes[0])[3:-1]))[1:-1])
    return config_list


def _get_ss_config(url, method='URL'):
    """
    抓取ss配置
    """
    res = ''
    while res == '':
        try:
            res = requests.get(url)
        except Exception as e:
            with open('{}/ss_log'.format(DIR_NAME), 'a') as l:
                l.write('ishadow打开失败: {}\n'.format(e))
                l.write('sleep {} seconds...\n'.format(TIME_SECONDS))
                sleep(TIME_SECONDS)
                l.write('retrying...')
    tree = etree.HTML(res.content)
    if method == 'URL':
        try:
            server_host = tree.xpath(r'//*[@id="ipsgc"]/text()')[0]
            server_port = int(tree.xpath(
                r'//*[@id="portfolio"]/div[2]/div[2]/div/div[9]/div/div/div/h4[2]/text()')[0].split('：')[-1])
            password = tree.xpath(r'//*[@id="pwsgc"]/text()')[0]
            method = tree.xpath(
                r'//*[@id="portfolio"]/div[2]/div[2]/div/div[9]/div/div/div/h4[4]/text()')[0].split(':')[-1]
        except Exception as e:
            with open('{}/ss_log'.format(DIR_NAME), 'a') as l:
                l.write('正则出问题 or 网页出问题了')
    else:
        qrcode = '{0}{1}'.format(BASE_URL, tree.xpath(
            r'//*[@id="portfolio"]/div[2]/div[2]/div/div[9]/div/div/div/h4[5]/a/@href')[0])
        qr_img = requests.get(qrcode)
        if qr_img.status_code == 200:
            qr_path = '{}/qr_img.png'.format(DIR_NAME)
            with open(qr_path, 'wb') as i:
                i.write(qr_img.content)
        (method, password, server_host, server_port) = _qr_decode(qr_path)
        # 邮件给手机
        send_email('{}/qr_img.png'.format(DIR_NAME))
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
        l.write('获取配置成功: \n{}'.format(ss_config))
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
            l.write('创建配置文件失败: {}\n'.format(e))


if __name__ == '__main__':
    # ss_config = _get_ss_config(HEAD_PAGE, method='URL')
    ss_config = _get_ss_config(HEAD_PAGE, method=sys.argv[1])
    # 保存本地使用
    save_config(ss_config)
