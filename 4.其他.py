# 列表推导式，返回格式和 in 的一致
list = [1, 2, 3, 4, 5, 6]
a = [x*2 for x in list ]
print(a)

# 元组
tulpe1 = 1,2,3
print(type(tulpe1))
tulpe2 = (1,2,3)
print(type(tulpe2))
set1 = {1,1,3}
print(type(set1), ' ', set1)

dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)
"""
显示为字典
{'sape': 4139, 'guido': 4127, 'jack': 4098}
遍历如下
"""
for k,v in dict1.items(): 
    print(k,v)

keys = [x for x in dict1.keys()]
print(keys)
sape = dict1.get('sape')
print(sape)
dict1['cao'] = 'nima'
print(dict1)
del dict1['guido']
print(dict1)





# https://www.runoob.com/python3/python3-data-structure.html