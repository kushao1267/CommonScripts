#coding=utf-8
'''
------------整站抓取图片,使用gevent+requests异步下载方式------------------
1.lxml包xpath工具获取url,其中xpath从chrome开发者工具获取
2.使requests下载
3.正则爬取url所有图片
4.异步IO处理图片下载任务
'''
import re
import requests
import os,time
from lxml import etree
from gevent import monkey;monkey.patch_all()
import gevent

ISOTIMEFORMAT='%Y-%m-%d %X'

def print_node(node): #打印Element元素
    print "==============================================" 
    print "node.attrib:%s" % node.attrib 
    print "node.attrib['href']:%s" % node.attrib['href'] 

def get_urls(root_url,numth_url):
    urls = set()
    res = requests.get(numth_url)
    selector = etree.HTML(res.content)
    #------取中文标题------"
#     //*[@id="gotop"]/div[2]/div/div/div[3]/div/ul/li[6]/a/text()
#     pic_name = selector.xpath("//*[@id='gotop']/div[2]/div/div/div[3]/div/ul/li/a/text()")
#     for i in pic_name:  #对应的url中文标题
#         print i
    pic = selector.xpath("//*[@id='gotop']/div[2]/div/div/div[3]/div/ul/li/a")
    for node in pic:    #获取自拍区第一页所有urls
        urls.add(root_url+node.attrib['href'])        
    print '抓取url数量:',len(pic)
    return (len(pic),urls)


def get_pic_url(url):   #获取指定url下的所有图片url
    res = requests.get(url)
    #图片所在标签: <a href=""><img src="" alt=""/></a></P>    
    pic_urls = re.findall(r'<a href=".+?"><img src="(.+?)" alt=".+?"/></a></P>', res.content, re.S) #正则匹配
    print '图片url:',pic_urls,'\n图片数量:',len(pic_urls)
    return pic_urls if len(pic_urls)<=10 else pic_urls[:10]    #只取前10个,因为很多重复的图片
        
def download(url):#图片下载
    url = re.sub(r'%2[eE]','.',url,re.IGNORECASE)   #如果.被编码为%2E则改回.
    res = requests.get(url)
#     print res.status_code
#     print res.encoding
    print '正在下载图片:'+url
    name=re.split(r'\.|/+',url) 
    filesavepath = os.getcwd()+'/49vvpic/'+name[-3]+time.strftime(ISOTIMEFORMAT,time.localtime( time.time()))+'.'+name[-1]
    with open(filesavepath,'wb') as f:#图片下载
        f.write(res.content)

if __name__=='__main__':
    #获取root_url
    r = requests.get('http://www.bg6f.com/404.html?/')
    root_url = re.findall(r'<div class=".*?">.*?<a href=".*?">(.*?)</a><a tppabs=".*?" target=".*?" href=".*?"><img src=".*?" tppabs=".*?"/></a></div>', r.content, re.S)
    print root_url
    number = raw_input('爬取第几页?:')
    #http://www.c53x.com/AAtupian/AAtb/zipai/index.html   首页
    #首页index,第二页index-2,第三页index-3...
    number ='' if number == '1' else '-'+number    
    numth_url = root_url[0]+'AAtupian/AAtb/zipai/index'+number+'.html'
    print numth_url
    #解决有时返回0个url的情况
    while True:      
        (numofurl,urls) = get_urls(root_url[0],numth_url)
        if numofurl != 0:
            break
        
    for url in urls:
        pic_urls = get_pic_url(url)         #正则爬取图片url
        gevent.joinall([gevent.spawn(download,pic_url) for pic_url in pic_urls])
    print '下载完成!!'
    
        
    
