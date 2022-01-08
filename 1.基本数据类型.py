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

print('-----------------------------')  # 数组
list = ['abc', 123, 'runoob', 10.2]
tinylist = ['a123', 456]
print(list)
print(tinylist)
print(list[0])
print(list[1:3])
print(list + tinylist)
print(list * 2)
list[1] = 456;
# 修改数组
print(list)

#元组,不可以改变属性，但是可以放数组对象进来改实参值
print("\n--------------------------------------")
tulpn = (1, 3, 2.2, '元组')
print(tulpn)
print(tulpn[0])
print(tulpn[1:-1])


#set 自动去重
site={'google', 'taobao', 'runoob', 'zhihu', 'baidu', 'baidu'}
print("\n--------------------------------------")
print(site)
if 'taobao' in site:
    print('taobao in site')
else:
    print('taobao not in site')

a=set('abcdefff')
b=set('bcde')

print('差集,a-b剩下的:', a - b)
print('交集,同时存在:', a & b)
print('并集:', a | b)
print('对称差集，两边都不同时存在:', a ^ b)

#字典（hashmap）
dict = {}
dict['key'] = 'value'

tinydict = {'key':'value', 'code':1, 'site':'www.baidu.com'}
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
if 2==2:
    print('判断')


"""
左移运算符，num << 1   相当于num乘以2
"""


