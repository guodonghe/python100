# 乘法口诀
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {}".format(j,i,i*j),end=" ")
    print (" ")
'''
# 水仙花数
for i in range(100,1000):
    a = int(i/100)
    b = int(i%100/10)
    c = int(i%10)
    if pow(a,3) + pow(b,3) + pow(c,3) == i:
        print (i)
