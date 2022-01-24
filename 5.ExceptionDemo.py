
class myException(Exception):
    def __init__(self, value):  
        self.value = value
    def __str__(self):
        return repr(self.value)


x = 10
# if x > 5:
    # raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

try:
    a = 3/0;
except Exception as ex:
    print('报错了：', ex)
else:
    print("没报错")
finally:
    print("必然只想finally代码")
    
