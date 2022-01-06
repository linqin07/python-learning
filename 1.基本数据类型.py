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
print("--------------------------------------\n")
tulpn = (1, 3, 2.2, '元组')
print(tulpn)
print(tulpn[0])
print(tulpn[1:-1])


