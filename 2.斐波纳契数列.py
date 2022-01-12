a, b = 0, 1
while (b < 10):
    print(b, end=',')
    # a, b = b, a + b
    b = a + b
    a = b

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2 == 1:
    print("2 - if 表达式条件为 true")
    print(var2)
elif var2 == 2:
    print('elif')
else:
    print('else')
print("Good bye!")

# 三目运算，true都结果 if 条件 else false都结果
print('True' if True else 'False')

print()
print('-------------------0累计到100------------------------')
print()

sum = 0
j = 0
while j <= 100:
    sum += j
    j = j + 1

print('sum=', sum)

# while 1 :print('百万富翁')

print()
print('Good bye!')

list = ('1', '2', '3', '4', '5')
for i in list:
    pass
    print(i)
    # break
    # continue

print("-----------iter--------------------")
import sys
list = [1, 2, 3, 4, 5]
it = iter(list)
print(next(it))

# for x in it:
#     print(x, end=', ')

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit

print('-----------------------------------------')
print()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self;
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()




  


