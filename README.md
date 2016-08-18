# Extract_urls
一个脚本:\n
*****************************************\n
*功能: \n
*1.提取参数,如:python Extract_urls.py -h中的h进行处理\n                 
*2.打开保存url的文件,with...as...方式\n
*3.从url中提取首页,正则表达式\n
*4.将首页地址保存到数据库(MySql/MongoDB)\n
*5.gevent+requests异步下载首页内容html\n
*6.爬取页面图片作为附件\n
*7.将附件和html通过smtp邮件发送\n
*****************************************\n
\n
urls.txt文件(与脚本在相同路径下)格式如下:\n
------------------------------------\n
http://www.kingdee.com/&user=339\n
http://www.kingdee.com/index\n
asdasd\n
http://www.baidu.com/admin\n
111http://www.baidu.com/upload\n
fggdfghttp://www.baidu.com/login\n
http://www.kingdee.com/login\n
a\n
http://www.sina.com.cn\n
------------------------------------\n
