# 第一个参数self(换其他名词也可以) 等同于 java的this对象，代表类实例
class MyClass:
    i = 123;

    def __init__(self) -> None:
        print(self)
        print(self.__class__)
        print(id(self))
        __age=18;
        pass
    def method(self):
        print('__age=', self.__)
        return 'hello'
    
x = MyClass()
print('x.i', x.i)
print('x.method', x.method())



