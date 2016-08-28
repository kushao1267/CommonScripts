#coding=utf-8
'''
装饰器: 
1.同时实现@log与@log()
2.实现@performance
python中,一切皆对象,函数也是对象.
因此def func().我可以将函数赋值给一个变量,如f=func
'''
import functools,time
#给func打log,,log('execute')(func)(6)可以执行下面的函数
def log(text_or_func):
    if type(text_or_func)==str: #callable(text_or_func)判断也可以
        def decorator(func):
            @functools.wraps(func)  #放在func的包装层
            def wrapper(*args, **kw):
                print '%s %s() result is:' % (text_or_func, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator
    else :
        @functools.wraps(text_or_func)
        def wrapper(*args,**kw):
            print "call %s():"%text_or_func.__name__
            return text_or_func(*args,**kw)
        return wrapper

#测试函数性能   
def performance(func): 
    @functools.wraps(func)
    def wrapper(*args,**kw):
        t1 = time.time()
        r = func(*args,**kw)    
        t2 = time.time()
        print 'call %s in :%s'%(func.__name__,t2-t1)
        return r
    return wrapper
    
'''
把@log放到func()函数的定义处，相当于执行了语句：
now = log(now)
'''
@log('execute') #@log/@log()均可
def func(num):
    return num+5

@performance
def func1(num):
    return num*num

print func(6)
print func1(6)


'''
func.__name__=wrapper,改变了函数的__name__属性,这不是我们想要的.
有些依赖函数__name__的代码执行会出错
functools可以很好的解决这个问题
'''
# print func.__name__

