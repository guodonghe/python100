# 无序表查找
def sequentialSearch(alist,item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

alist = [3,5,9,12,15,19,21]
print(sequentialSearch(alist,19))
print (sequentialSearch(alist,18))

# 有序表查找
def ordersequentialSearch(alist,item):
    pos = 0
    found = False
    step = False
    while pos < len(alist) and not found and not step:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                step = True
            else:
                pos += 1
    return found
orderlist = [3,5,9,12,15,19,21]
print (ordersequentialSearch(orderlist,15))
print (ordersequentialSearch(orderlist,10))
