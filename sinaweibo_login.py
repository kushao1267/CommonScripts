#coding=utf-8
import requests
import sys
#一 使用post提交表单登陆，会被sina visitor system拦截（首次登陆都会进入到这里）不可行
'''
s = requests.session()
data = {'username':'xxx','password':'xxx'}
#post 换成登录的地址，因为要提交的是账号密码，所以不能在url中提交，而是以post表单的方式。
res=s.post('http://weibo.com/',data=data);
#换成抓取的地址
res = s.get('http://weibo.com/');
print type(res)
try:
    file = open('weibo.html','w')
    try:
        file.write(unicode(res))
    finally:
        file.close()
except IOError:
    print 'failed to open file!'

print res.text
'''

#二 使用cookies模拟登陆sina微博，get方法，缺点是每过一段时间cookies就会变化
#使用HttpFox获取登陆后的cookies
COOCKIE = ''
url = 'http://weibo.com/'
cookies={}  
for line in COOCKIE.split(';'):  
    key,value=line.split('=',1)#1代表只分一次，得到两个数据  
    cookies[key]=value 
s = requests.session()
res = s.get(url,cookies=cookies)
#将get的文件
try:
    file = open('weibo.html','w')
    try:
        file.write(res.text.encode('utf8'))
    finally:
        file.close()
except IOError:
    print 'failed to open file!'
#print res.text#打印微博登陆的首页
 