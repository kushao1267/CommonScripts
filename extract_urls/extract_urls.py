#coding=utf-8
'''
*****************************************
*功能: 
*1.提取参数,如:python extract_urls.py -h中的h进行处理                         
*2.打开保存url的文件,with...as...方式
*3.从url中提取首页,正则表达式
*4.将首页地址保存到数据库(MySql/MongoDB)
*5.gevent+requests并发下载首页内容html
*6.爬取页面图片作为附件
*7.将附件和html通过smtp邮件发送
*****************************************
urls.txt文件格式如下:
------------------------------------
http://www.kingdee.com/&user=339
http://www.kingdee.com/index
asdasd
http://www.baidu.com/admin
111http://www.baidu.com/upload
fggdfghttp://www.baidu.com/login
http://www.kingdee.com/login
a
http://www.sina.com.cn
------------------------------------
'''

import re
import os
import sys
import MySQLdb
import pymongo
import time
import smtplib
import requests
import gevent
from gevent import monkey;monkey.patch_all()
from email.mime.text import MIMEText

def argv_operate(argv):
    name = argv[0]
    if len(argv)==1:
        print '-------------------------------------------------------'
        print "Hello,this is liujian's script"
        print '-------------------------------------------------------'
    elif argv[1] == '-v' or argv[1] == '-version':
        print '-------------------------------------------------------'
        print 'Name:'+str(name)+'\nVersion :1.0'+'\nUsed to extract urls from a file!'
        print '-------------------------------------------------------'
    elif argv[1] == '-h' or argv[1] == '-help':
        print '-------------------------------------------------------'
        print 'This script have openfile and extract urls functions!'
        print 'def extract(urls):'
        print 'file_open(filename):'
        print '-------------------------------------------------------'
    else:
        print '-------------------------------------------------------'
        print 'Wrong Argument!please input again!'
        print '-------------------------------------------------------'
        
def file_open(filename):
    BasePath = os.getcwd()  #获得当前工作目录
    path = BasePath + '/'+filename+'.txt'
    print path+'是目录?:'+str(os.path.isdir(path))
    print path+'是文件?:'+str(os.path.isfile(path))
    print path+'是绝对路径?:'+str(os.path.isabs(path))
    print '工作目录:'+BasePath
    #with的对象必须有一个__enter__()方法，一个__exit__()方法
    with open(path,'r') as f:
        #文本方式读取到文件内容很有可能会比二进制文件短，因为文本方式读取要把回车，换行两个字符变成一个字符
        #所以文本的最好用r,二进制的最好用rb
        urls = f.readlines()
    return urls

def extract(urls):
    #敏感字符要转义如:.*?\等,转移符号和\w\s\d符号都是用'\'而不是'/',如果有()|(),记得在他们的外面加()
    pa = re.compile(r'http://w{3}\.\w+\.((\w+\.\w+)|(\w+))',re.I|re.M)    
    res = set()     #保存结果
    for i in urls:
        r = re.search(pa, i)
        if r:   #排除其他字符串干扰
            res.add(r.group())
    print res
    return res

def saved(res,database='1',db_name='test',username='root',passwd='xx'):    #保存到数据库,mysql或mongodb
    if database=='1':
        try:
            conn = MySQLdb.Connection(user=username,passwd=passwd,db=db_name,use_unicode=True)
            cursor = conn.cursor()      #获取cursor
            cursor.execute('drop table urls')   #删除上次的表varchar(10)
            cursor.execute('create table if not exists urls(ID tinyint primary key,URL varchar(50),CTIME timestamp not null default current_timestamp)')
            k=0
            for i in res:
                k+=1
                #只能用%s作为占位符,即使是int类型
                cursor.execute("insert into urls (ID,URL) values (%s,%s)",[str(k),i])
            cursor.execute('select * from urls')
            return True
        except Exception,e:
            print e
            return False 
        finally:
            cursor.close()
            conn.close()    
    else :  #使用mongodb
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        try:
            conn = pymongo.MongoClient(host='localhost',port=27017)
            db = conn[db_name]
            coll = db['urls']
            #coll.drop()     #删除上次保存的url表格
            coll.remove()   #删除url表格中的记录
            for i in res:
                coll.insert({'URL':i,'CTIME':time.strftime( ISOTIMEFORMAT, time.localtime( time.time()))})
        except Exception,e:
            print e
        finally:
            conn.close()
        return True

def download(url):
    if not url.startswith('http://'):   #没有http头,urllib和requests都不能运行
        url='http://'+url
    #requests的text获取到的是unicode,content取到的是网页自带的编码str;urllib2获取的是网页自带的编码str
    data = requests.get(url).content    
    
def down_manager(urls):
        gevent.joinall([gevent.spawn(download,i) for i in urls])    #spawn(func,arg)
        
        data = requests.get(urls.pop()).content    #取最后一个url的html页面返回
        return data

def send_email(mail_host,fromwho,password,towho,content):   #content:html/文本
    #构建MIME
    msg = MIMEText(content,'html','utf-8')
    msg['Subject']='hello'
    msg['From']=fromwho
    msg['To']=towho
    try:
        server = smtplib.SMTP(mail_host)#创建服务
        server.set_debuglevel(1)#调试模式:会话过程中会有输出信息
        server.login(fromwho,password)#登陆
        server.sendmail(fromwho,towho,msg.as_string())#发送
        server.close()#关闭
        return True
    except Exception,e:#异常
        print str(e)
        return False
        
if __name__=='__main__':
    #------------输入sys参数------------
    argv_operate(sys.argv)
    #------------打开文件------------
    urls = raw_input('请输入文件名:')  #raw_input把输入作为字符串,而input根据输入做类型转换
    urls = file_open(urls)
    #------------提取url------------
    res = extract(urls)
    #------------保存url------------
    database = raw_input('请输入要使用的数据库(1:mysql,2:MongoDB):')
    db_name = raw_input('请输入db?:')
    username = raw_input('账户:')
    passwd = raw_input('密码:')
    if saved(res):
        print '保存成功'
    else:
        print '保存失败'
    #------------下载(gevent+requests并发)------------
    flag = raw_input('是否下载? (Y/YES):')
    if re.match(r'y|yes',flag,re.I):
        content = down_manager(res)
    else:
        print '你选择不下载!'
    #发送邮件
    mail_host='smtp.aliyun.com'
    fromwho = 'xx@aliyun.com'
    password = 'xx'
    towho = 'xx@qq.com'
    print content
    if send_email(mail_host,fromwho,password,towho,content):
        print '发送成功!'
    else:
        print '发送失败!'
    
    
    
    
