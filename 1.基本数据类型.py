a = 1
b = 1.1
c = True
d = '字符串'

print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))


class A:
    pass


class B(A):
    pass  # isinstance() 会认为子类是一种父类类型


print(isinstance(B(), A))  # True# type() 不会认为子类是一种父类类型
print(type(A()) == A)  # True
print(isinstance(A(), A))  # True
print(type(B()) == A)  # Fale

print(issubclass(bool, int))

var1 = 11
del var1

5 + 4

# 多个同时赋值
a, b = 1, 2

print('-----------------------------')  # 数组，左闭右开
list = ['abc', 123, 'runoob', 10.2]
tinylist = ['a123', 456]
print(list)
print(tinylist)
print(list[0])
print(list[1:3])
print(list + tinylist)
print(list * 2)
list[1] = 456
# 修改数组
print(list)

#元组,不可以改变属性，但是可以放数组对象进来改实参值
print("\n--------------------------------------")
tulpn = (1, 3, 2.2, '元组')
print(tulpn)
print(tulpn[0])
print(tulpn[1:-1])

#set 自动去重
site = {'google', 'taobao', 'runoob', 'zhihu', 'baidu', 'baidu'}
print("\n--------------------------------------")
print(site)
if 'taobao' in site:
    print('taobao in site')
else:
    print('taobao not in site')

a = set('abcdefff')
b = set('bcde')

print('差集,a-b剩下的:', a - b)
print('交集,同时存在:', a & b)
print('并集:', a | b)
print('对称差集，两边都不同时存在:', a ^ b)

#字典（hashmap）
dict = {}
dict['key'] = 'value'

tinydict = {'key': 'value', 'code': 1, 'site': 'www.baidu.com'}
print(dict['key'])
print(tinydict)
print(tinydict['site'])
print(tinydict.keys())
print(tinydict.values())

# 运算符号，+-*/ % += -=
"""
运算符号基本和java一样，除法 / 默认是算到小数
此外还支持 2 ** 3 = 8 平方运算，3 // 2 = 1 除法向下取整
"""
if 2 == 2:
    print('判断')
"""
左移运算符，num << 1   相当于num乘以2
右移运算符，num >> 1   想等于num除以2
& 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
| 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
^ 按位异或运算符：当两对应的二进位相异时，结果为1
~ 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
a = 0011 1100
b = 0000 1101
--------------------
&   0000 1100     = 12
|   0011 1101     = 61
^   0011 0001     = 49
~a  1100 0011     = -61
b >> 1
    0000 0110    等于除2向下取整
"""

a = 60
b = 13
c = 0

print('与&：', a & b)
print('或|：', a | b)
print('异或^：', a ^ b)
print('非~：', ~a)
print('左移<<:', a << 1)
print('右移>>:', b >> 1)

new_var = {1, 2}
tuple1 = ('1')
list1 = [1, 2]
if 1 in new_var:
    print(1)
if 1 in list1:
    print('list', 1)
if '1' in tuple1:
    print('tuple1', 1)

aa = 1
bb = 1

if aa is bb:
    print('is 比较对象引用')
if aa == bb:
    print('== 比较值')

print(list1[:])

# 格式化
print('我叫 %s 今年 %d 岁' % ('小米', 12))
# f_string
name = 'cainiao'
print(f'hello {name}')
w = {'name': 'cainiao', 'url': 'www.cainiao.com'}
print(f'{w["name"]}:{w["url"]}')

x = 1
print(f'{x+1=}')

str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

print('count:', str.count('菜鸟', 0, 3))
print('endwith', str.endswith('教程'))

low = 'str'
print('首字母大写', low.capitalize())
print(low.find('t', 0, 3))
print(low.rfind('t'))
print(low.index('t'))
print(low.lower())
print(low.upper())
print('最少一个字符或者数字的类型', low.isalpha())
print('判断是否为数字', low.isdecimal)
print(max(low))
print(min(low))

L = ['1', '2', 3, 4, 4]
newL = ['11', '22']
print('list count', L.count(4))
L.append(5)
L.extend(newL)
print(L)
print('查找位置:', L.index(4))
L.insert(0, '0')
L.pop(-1)
#移除最后一个
L.remove('1')
# 移除第一个值是1的
print(L)
L.reverse()
print(L)
L.sort(reverse=True)  #不可以混着类型排序
