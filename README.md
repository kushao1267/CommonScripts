#Common Python Scripts

###目录:

```
    1.extract_urls 
    2.craw_pic 
    3.zodiac 
    4.mongoDB_use 
    5.sinaweibo_login 
    6.sort_method
    7.decorator
    8.pointer_operation
    9.big_data
    10.my_profile
    11.algorithms
    12.short_path
    13.plot_excel
    14.async_aiohttp_craw
    15.moctest.py
    16.shadowsocks
```


###1.extract_urls:一个提取url首页进行各种处理的脚本
```
功能: 
    - 提取参数,如:pythoon extract_urls.py -h中的h进行处理    
    - 提取所有urls的首页并去重,正则表达式 
    - 将首页地址保存到数据库(MySql/MongoDB) 
    - gevent+requests异步下载首页内容html 
    - 将首页内容html通过smtp邮件发送
    
# urls.txt(与脚本在相同路径下):
    http://www.kingdee.com/s?a=b 
    http://www.kingdee.com/index 
    asdasd 
    http://www.baidu.com/admin 
    111http://www.baidu.com/upload 
    fggdfghttp://www.baidu.com/login 
    http://www.kingdee.com/login 
    a 
    http://www.sina.com.cn 

待解决问题: 
    1.爬取图片并作为邮件附件发送</br>
    2.解决"被认定为垃圾邮件" `
```


###2.craw_pic:抓取某x0网站xx区全部图片
```
功能: 
    - lxml包xpath工具获取url,其中xpath从chrome开发者工具获取.
    - 正则爬取url所有图片url.
    - 用gevent+requests并发下载图片.
    - 使用代理socks5.
    - tqdm(进度条)因对python3.5兼容不好，已经移除.
已经解决:
    1.因用当前时间命名导致文件覆盖的问题 
    2.可以下载不同区的所有图片 
待解决问题:
    1.处理内容重复的图片 </br>
    2.网址挂掉如何使用它的备用网站(代码已写等它挂) 
```

###3.zodiac:根据日期计算星座 
```
功能:  
    - 计算星座 
    - 处理边界条件 
```

###4.mongoDB_use:pyMongo的使用总结
```
功能:  
    - pyMongo的使用总结 
    - 增删查更 
```


###5.sinaweibo_login:新浪微博模拟登陆,POST方式和cookie方式
```
功能:  
    - 新浪微博模拟登陆,POST方式 
    - 新浪微博模拟登陆,cookie方式 
待解决问题: 
    1.POST方式会被重定向,通过接入sina API可以使用POST方式进入真正的主页 
```


###6.sort_method:完成6种排序算法
```
功能: 
    - python完成六种排序算法   
说明：
    - 调用快排 
    - 归并排序 
    - 选择排序 
    - 插入排序 
    - 冒泡法      
    - 桶排序 
```


###7.decorator:装饰器 
```
功能:
    - 装饰器decorator 
说明：
    - 同时实现@log与@log() 
    - 实现@performance
```


###8.pointer_operation: Python版的结构体指针操作,之前用C写了一遍，现在再熟悉一下
```
功能:
    - 链表指针操作  
说明：
    - 初始化链表
    - 插入元素 
    - 删除元素
    - 遍历链表
    - 反转链表
    - 合并有序链表
    - 查找两个链表的交点
待解决问题: 
    1.链表是否成环 
    2.环的入口
```


###9.big_data
```
功能：
    - 机器学习与大数据分析,主要是numpy/pandas/skilearn/scipy几个库的使用．
流程：
    - 数据爬取->加载->归一化->特征选择->RFE建模->ML分类算法->参数优化
说明：
    - 加载*.csv数据文件
    - 各种skilearn中包含的经典Machine Learning分类算法
    - 参数优化模型
```


###10.my_profile
```
功能:
    - 对python脚本运行时间profile,测试性能瓶颈.
使用方式：
    - 命令行输入python my_profile -p xxx.py，将输出报告到屏幕.
    - 使用python内置模块pstats.
```


###11.algorithms
```
功能：
    - 常见的面试算法题解答，python版
题目名：
    - partition
    - median
    - small k
    - quicksort
    - the first number which apear once
    - implement add without '+ - * /'
    - fib
    - Clockwise matrix printing
    - number of '1'
    - let odd before even in a list
    - DFS
    - BFS
    - binary tree
```


###12.short_path
```
说明：最短路径算法
    - 松弛技术
    - Bellman-Ford算法
    - Dijkstra算法
    - Johnson,基于多对多的稀疏图
    - Floyd Warshall，仅考虑距离
```


###13.plot_excel  
```
功能：
    - 使用xlsxwriter模块完成生成excel表，画图表.
函数:
    - ExcelGeneratorw生成excel表
    - Ploter画图表
```


###14.async_aiohttp_craw
```
功能：
    - asyncio，aiohttp完成异步爬取
    - 特点是能够高并发爬取大量数据。
```


###15.moctest
```
功能：
    - unittest与moc实现单元测试
    - moc用于模仿第三方服务的返回值，省去等待响应时间
    - moc.patch()与moc.patch.object()
```

###15.shadowsocks
```
文件:
    ssstart.py 
    ssconfig.py
要求:
    pip安装pysocks,requests,lxml
    安装shadowsocks客户端
    python3环境
功能：
    创建ss配置并修改权限.
    支持使用自己的ss,修改ssconfig.py中的select_point['0']即可.
    支持使用的免费ss.
使用:
    sudo python ssstart.py
    
    ps: 
        1,2,3 选项:使用免费ss;
        0 选项:使用自己的ss;
```