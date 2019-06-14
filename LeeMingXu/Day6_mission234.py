import math
def hws(num):
    ls = list(num)
    if int(num)==int(''.join(reversed(ls))):
        return True
    else:
        return False
def ss(num):
    for each in range(2,int(math.sqrt(int(num)))):
        if int(num) % each == 0:
            return False
    fnum = int(str(''.join(reversed(list(str(num))))))
    for each in range(2,int(math.sqrt(fnum))):
        if fnum % each == 0:
            return False
    return True
a = input('请输入一个数字：')
if hws(a):
    print("{0}是回文数".format(a))
else:
    print("{0}不是回文数".format(a))
if ss(a):
    print("{0}是真素数".format(a))
else:
    print("{0}不是真素数".format(a))