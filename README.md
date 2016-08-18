<html>
<body>
<p>
# Extract_urls<br/>
一个脚本:<br/>
****************************************************<br/>
*功能: <br/>
*1.提取参数,如:pythoon Extract_urls.py -h中的h进行处理<br/>                 
*2.打开保存url的文件,with...as...方式<br/>
*3.从url中提取首页,正则表达式<br/>
*4.将首页地址保存到数据库(MySql/MongoDB)<br/>
*5.gevent+requests异步下载首页内容html<br/>
*6.爬取页面图片作为附件<br/>
*7.将附件和html通过smtp邮件发送<br/>
****************************************************<br/>
<br/>
urls.txt文件(与脚本在相同路径下)格式如下:<br/>
---------------------------------------------<br/>
http://www.kingdee.com/s?a=b<br/>
http://www.kingdee.com/index<br/>
asdasd<br/>
http://www.baidu.com/admin<br/>
111http://www.baidu.com/upload<br/>
fggdfghttp://www.baidu.com/login<br/>
http://www.kingdee.com/login<br/>
a<br/>
http://www.sina.com.c<br/><br/>
---------------------------------------------<br/>

</p>

</body>
</html>
