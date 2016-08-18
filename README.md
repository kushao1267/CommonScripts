# Extract_urls
一个脚本:
*****************************************
*功能: 
*1.提取参数,如:python Extract_urls.py -h中的h进行处理                         
*2.打开保存url的文件,with...as...方式
*3.从url中提取首页,正则表达式
*4.将首页地址保存到数据库(MySql/MongoDB)
*5.gevent+requests异步下载首页内容html
*6.爬取页面图片作为附件
*7.将附件和html通过smtp邮件发送
*****************************************

urls.txt文件(与脚本在相同路径下)格式如下:
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
