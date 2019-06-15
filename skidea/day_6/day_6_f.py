import math
def su(a):
    if int(a)>3:
        for num in range(2,int(math.sqrt(int(a)))+1):
            if int(a)%num==0:
                break
        if int(a)%num==0:
            return False
        else:
            return True
    else:
        return False
def ppp(a):
    num=0
    for char in a:
        if(a[-(num+1)])!=char:
            continue
        num+=1
    if char==a[0] and char==a[-1]:
        print('yes')
    else:
        print('no')