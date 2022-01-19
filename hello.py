import keyword
from typing import Sequence
print('hello world')

# 这是注释
print(keyword.kwlist)

if False:
    print('True')
else:
    print('false')
    print ("False") 

# r 表示raw String，显示原文
print(r'this is a \nstring!')

word = '字符串'
juzi = '这是一个句子。'
paragraph = """PS D:\python-learning> & D:/python/python.exe 这是段落
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32"""

str='123456789'
print(str)
print(str[0:-3]) #第1到砍掉后面3个
print(str[1])    #第二个字符

print(str[1:])   #第一个到最后
print(str[1:5])  #第一个到第五个（不算）
print(str[1:5:2])  #第一个到第五个（不算），步长2

# input(r'\n\n 按下enter后退出')

import sys; x = "菜鸟"; sys.stdout.write(x+'\n')

print(1111, end='')
print(2222)

# improt --------
import com.fib as fib
fib.fib(14)

print('dir():', dir())
    





