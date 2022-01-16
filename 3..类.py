# 第一个参数self(换其他名词也可以) 等同于 java的this对象，代表类实例
class MyClass:
    i = 123;

    def __init__(self) -> None:
        print(self)
        print(self.__class__)
        print(id(self))
        pass
    def method(self):
        return 'hello'
    
x = MyClass()
print('x.i', x.i)
print('x.method', x.method())


#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print("%s 说: 我 %d 岁, %d kg。" %(self.name,self.age, self.__weight))
 
# 实例化类
p = people('美女', 24, 50)
p.speak()
print(p.name, p.age, '岁')

class animal(people):
    def speak(self):
        return super().speak()
    def run(self):
        print('name run', self.name)

animal = animal('动物', 10, 20)
animal.speak()
print(animal.name, animal.age)



#可写函数说明,指定顺序.指定默认值
def printinfo(age, name='qin'):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return 
printinfo(age=50, name='lin')
# print()
printinfo(age=10)


# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。加了两个星号 ** 的参数会以字典的形式导入
def printInfo(a, *b):
    print('不定长输出:', type(b))
    print('a=', a, ',', 'b')

printInfo('a', 'b', 'c')

def printInfo(a, **b):
    print('不定长输出:', type(b))
    print('a=', a, ',', b)
    return
printInfo('a', x=1, b=2)

# python 使用 lambda 来创建匿名函数
sum = lambda args1, args2 : args1 +args2; 
print(sum(1,3))





