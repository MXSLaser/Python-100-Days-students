"""
更相减损术
"""
import math
def ppp(a,b):
    Max=1
    c=a if a<b else b
    for num in range(2,c+1):
        if num==c:
            break
        if a%num==0 and b%num==0:
            a=a/num;b=b/num
            Max=Max*num
    Min=Max*a*b
    print('最大公约数',Max)
    print('最小公倍数',Min)

a=int(input('请输入数字'))
b=int(input('请输入数字again'))
ppp(a,b)

