#coding=utf-8
'''
Author:LiuJian
Data:2016.09.19

function:
    命令行输入python my_profile -p xxx.py
    cprofile对xxx.py进行性能测试,并打印报告
'''
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-p' ,dest = 'profile', help = 'Profile the program')
args = parser.parse_args()
myprofile = args.profile
if myprofile is None:
    print args['-h']
    exit(0)

#profiling
cmd1 = 'python -m cProfile -o test.out '+myprofile
cmd2 = '''python -c "import pstats; p=pstats.Stats('test.out'); p.sort_stats('time').print_stats()"'''

#1.os方式
if os.system(cmd1)!=0:
    print 'failed to output *.out file.'
    exit(0)
if os.system(cmd2)!=0:
    print 'failed to open test.out'
    exit(0)
     
# #2.subprocess方式
# comRst1 = subprocess.Popen(cmd1,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# (m_stdout1, m_stderr1) = comRst1.communicate()
# print m_stdout1
#  
# comRst2 = subprocess.Popen(cmd2,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# (m_stdout2, m_stderr2) = comRst2.communicate()
# print m_stdout2
    