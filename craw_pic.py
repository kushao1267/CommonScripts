#coding=utf-8
'''
********整站抓取图片,使用gevent+requests异步下载方式********
*1.lxml包xpath工具获取url,其中xpath从chrome开发者工具获取
*2.使requests下载
*3.正则爬取url所有图片
*4.协程处理图片下载任务
*5.tqdm显示进度
*6.自动打开文件夹窗口展示图片
'''
import re
import requests
from tqdm import *
import os
import time
from lxml import etree
from gevent import monkey;monkey.patch_all()
import gevent

#--------创建路径,储存图片------------
BASEPATH = os.getcwd()+'/49vvpic/'
ORIGIN_URL = 'http://www.bg6f.com/404.html?/'

def get_urls(root_url,numth_url):
    res = requests.get(numth_url)
    selector = etree.HTML(res.content)
    #------取中文标题------"
    pic_name = selector.xpath("//*[@id='gotop']/div[2]/div/div/div[3]/div/ul/li/a/text()")
    pic = selector.xpath("//*[@id='gotop']/div[2]/div/div/div[3]/div/ul/li/a")
    #将url名与对应的url进行打包
    urls = zip(pic_name,[root_url+node.attrib['href'] for node in pic])
    return (len(pic),urls)

def get_pic_url(url):   #获取指定url下的所有图片url
    res = requests.get(url)
    #图片所在标签: <a href=""><img src="" alt=""/></a></P>    
    pic_urls = re.findall(r'<a href=".+?"><img src="(.+?)" alt=".+?"/></a></P>', res.content, re.S) #正则匹配
    print '\n图片数量:',len(pic_urls)
    return pic_urls if len(pic_urls)<=10 else pic_urls[:20]    #每个网页最多下20张,因为很多重复的图片
        
def download(title,url):#图片下载
    url = re.sub(r'%2[eE]','.',url,re.IGNORECASE)   #如果.被编码为%2E则改回.
    res = requests.get(url)
#     print res.status_code
#     print res.encoding
    print '正在下载图片:'+url
    name=re.split(r'\.|/+',url) 
    filesavepath = title+name[-3]+str(time.time())+'.'+name[-1]
    with open(filesavepath,'wb') as f:#图片下载
        f.write(res.content)

def choose(root_url):
    print '亚洲:asia,欧美:oumei,自拍:zipai,美腿:meitui,动漫:cartoon'
    areas = ['asia','oumei','zipai','meitui','cartoon']
    while True:
        area = raw_input('看什么区?请输入拼音:').strip()
        if area in areas:
            break
    number = raw_input('爬取第几页?:')
    #首页index,第二页index-2,第三页index-3...
    number ='' if number == '1' or number=='' else '-'+number    
    return root_url+'AAtupian/AAtb/'+area+'/index'+number+'.html'

def do_work(BASEPATH,urls):
    for pic_name,url in tqdm(urls):  #tqdm封装迭代器,显示进度
        title = BASEPATH+pic_name+'/'   #根据标题,创建子目录,易于区分图集
        print '\n开始下载:',pic_name
        if not os.path.isdir(title):
            os.mkdir(title)
        pic_urls = get_pic_url(url)         #正则爬取图片url
        gevent.joinall([gevent.spawn(download,title,pic_url) for pic_url in pic_urls])#gevent并发下载
    print '\n下载完成!!'
    
 
if __name__=='__main__':
    try:
        #从防黑页面获取root_url,防止网页挂掉
        r = requests.get(ORIGIN_URL)
    except Exception:
        print '网络链接失败!请检查网络:'
        exit(0)
    root_url = re.findall(r'<li>.*地址：<a href=".*?">(.*?)</a>&nbsp;',r.content,re.S)
    print 'root_url:',root_url
    #选择页面,第一页,第二页>..
    numth_url = choose(root_url[0])    
    print numth_url
    #解决指定页有时返回0个url的情况
    while True:      
        (numofurl,urls) = get_urls(root_url[0],numth_url)
        if numofurl != 0:
            break
    #创建根目录
    if not os.path.isdir(BASEPATH):
        os.mkdir(BASEPATH)
        os.system('nautilus '+BASEPATH) #打开文件夹图像窗口
    #开始下载
    do_work(BASEPATH,urls)
    
        
    
