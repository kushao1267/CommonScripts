# coding=utf-8
"""
    批量下载百度图片某个topic下的图片：例如，美女
    
    解决Ajax请求数据(xhr)的爬取问题
    解决无浏览器UA被反爬虫禁的问题
    解决不带session请求页面的问题
    异步io加快图片下载速度
    
    可供修改参数:
        QUERY_WORD: 关键词
        PAGE_NUM: 初始图片序号，默认0
        MAX_ARRIVE_NUM: 最大图片序号，默认10000
"""

import re
import os
import time
from urllib.parse import quote
import requests
import gevent
from gevent import monkey


QUERY_WORD = "美女"  # 百度爬取关键词
DIR_NAME = os.getcwd() + "/baidu_beauty/"  # 图片文件夹名称

MAX_RANGE_NUM = 30  # rn参数，Ajax请求每页的图片数 (pn表示当前请求的图片序号，rn表示更新显示图片的数量)
PAGE_NUM = 0  # pn参数
MAX_ARRIVE_NUM = 10000  # 最大图片序号数

HEADERS = {  # 没有浏览器请求头会被反爬虫禁
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "img3.imgtn.bdimg.com",
    "If-Modified-Since": "Thu, 01 Jan 1970 00:00:00 GMT",
    "If-None-Match": "8cd510bc4e3cfb95598a189a5668b856",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "uMozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}


def get_more_page(word):
    """
    爬取更多的页面
    从百度图片上滑动时，Ajax加载的url，可以选择pn,rn参数用来指定要爬取的图片序号、个数
    页面中:第一张图序号为pn, 更新图数为rn
    """
    # Ajax url
    html = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=6&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word={}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&cg=girl&pn={}&rn={}&gsm=3c&1524209343246="
    more_pages = []
    for x in range(PAGE_NUM, MAX_ARRIVE_NUM, MAX_RANGE_NUM):
        html_new = html.format(quote(word), quote(word), x, MAX_RANGE_NUM)
        more_pages.append(html_new)
    return more_pages


def page_task(session, page):
    """
    每页的爬取任务，记录失败的页数，然后下次继续从该节点爬取
    """
    page_num = page.split("pn=")[-1].split("&")[0]
    result = _get_img_urls(session, page)  # 每页的图片url列表
    if result:
        gevent.joinall([gevent.spawn(_craw_pic, session, url, page_num)
                        for url in result])
    else:
        print("链接:{}\n未抓取到图片url".format(page))


def _get_img_urls(session, page):
    """
    获取每页的img url
    """
    r = session.get(page)
    result = []
    if r.status_code == 200:
        result = re.findall(r'''\[{"ObjURL":"(.*?)"''',
                            r.text, re.S)  # ObjURL高清图片
    return result


def check_directory(dir_name=DIR_NAME):
    """
        检查图片储存文件夹目录，不存在则创建
    """
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    print("图片储存在:", dir_name)


def _craw_pic(session, url, page_num, path=DIR_NAME):
    """
        爬取图片
    """
    url = url.replace("\\", "")  # 去掉转义符
    temp = url.split("u=")[-1]
    file_path = path + temp.split("&")[0] + temp.split(".")[-1]
    if os.path.isfile(file_path) is False:
        print("爬取: ", url)
        try:
            req = session.get(url, headers=HEADERS, timeout=8)
            if req.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(req.content)
                print("图片储存成功!")
        except Exception as e:
            print("任务失败，图片序号:{}\n错误原因:{}\n ".format(page_num, e))
    else:
        print("图片已存在!")

        
if __name__ == "__main__":
    monkey.patch_all()
    check_directory()
    with requests.Session() as session:
        session.get("https://www.baidu.com")
        more_pages = get_more_page(QUERY_WORD)
        for page in more_pages:
            page_task(session, page)
