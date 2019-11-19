# 求阶乘之和
# 解法一
sum = 0
factorial = 1
num = int(input('请输入一个数字: '))
for i in range(1,num+1):
    factorial = factorial * i
    sum += factorial
print ('阶乘之和: ',sum)

# 解法二
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
'''
list=[]
num = int(input('请输入一个数字: '))
for i in range(1,num+1):
    list.append(factorial(i))
print (sum(list))
'''
sum = 0
num = int(input('请输入一个数字: '))
for i in range(1,num+1):
    sum += factorial(i)
print (sum)

# 解法三
import math
sum = 0
num = int(input('请输入一个数字: '))
for i in range(1,num+1):
    sum += math.factorial(i)
print ('阶乘之和: ',sum)
