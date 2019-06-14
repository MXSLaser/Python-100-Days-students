"""
完美数，又称完全数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，
第三个完全数是496，后面的完全数还有8128、33550336等等。
输入：
输出：   6
        28
        496
        8128
"""
import math
num=0
b=3
number=4
while True:
    b2=0
    b=b+1
    for a in range(1,int(b)):
        if b%a==0:
            b2=b2+a;#print(b);print(b2);input()
            #print(b)
    if b==b2:
        num=num+1
        print(b)
    if num == number:
        break
