def gys(a,b):
    if a < b:
        temp = a
        a = b
        b = temp
    while a!=b:
        if a&1:
            if b&1:
                temp = a
                a = (a + b) >> 1
                b = (temp - b) >> 1
            else:
                b>>= 1
        else:
            if b&0:
                a >>= 1
                b >>= 1
            else:
                a >>= 1
                if a < b:
                    temp = a
                    a = b
                    b = temp
    return a
def gbs(a,b,gys):
    return a*b//gys
a = int(input('请输入第一个数:'))
b = int(input('请输入第二个数:'))
print('公约数:'+str(gys(a,b)))
print('公倍数:'+str(gbs(a,b,gys(a,b))))