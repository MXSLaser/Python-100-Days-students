from day_6_f import su
def zhensu(a):
    c=''
    m = 1
    for b in a:
        c += a[-m]
        m += 1
    if su(a) and su(c):
        print('yes')
    else:
        print ('no')

a=input('请输入一个数字')
zhensu(a)