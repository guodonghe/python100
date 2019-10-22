# 变形词实例 variant.py
def bxcword(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    #return matches
    if matches == True:
        print("s1与s2是变形词")
    else:
        print("s1与s2不是变形词")
              

bxcword('python','thonpy')
            
