# -*- coding: utf-8 -*-
"""
得到日期日期,计算星座
"""
#获得当前时间
import datetime
# Get a datetime object
now = datetime.datetime.now()
# General functions 
print "Year: %d" % now.year
print "Month: %d" % now.month
print "Day: %d" % now.day
print "Weekday: %d" % now.weekday()
# Day of week Monday = 0, Sunday = 6
print "Hour: %d" % now.hour
print "Minute: %d" % now.minute
print "Second: %d" % now.second
print "Microsecond: %d" % now.microsecond


#计算星座
def Zodiac(month, day):
  n = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
  d = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
  return n[len(filter(lambda y:y<=(month,day), d))%12]

def get_date():
    while True:
        month = raw_input('请输入月份?')
        month = int(month)
        if type(month) == int and month>0 and month<13:
            break
    while True:
        day = raw_input('请输入日?')
        day = int(day)
        if type(day) == int and day>0 and day<32:
            break
    return (month,day)    
        
if __name__=='__main__':
    (month,day)=get_date()
    print Zodiac(month,day)

