# 斐波那契数列
# 实现一
'''
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b,a+b
        print (a,end=" ")
        n += 1

fib(10)
'''
# 实现二

import sys
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b,a+b
        yield a
        n += 1


f = fib(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
