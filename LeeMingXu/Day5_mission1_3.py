'''
测试问题3：百鸡百钱
输入：无
预计输出：  公鸡0只 母鸡25只 小鸡75只
            公鸡4只 母鸡18只 小鸡78只
            公鸡8只 母鸡11只 小鸡81只
            公鸡12只 母鸡4只 小鸡84只
'''
x=0
y=0
z=100-x-y
while x*5<100:
    for y in range(0,(100-5*x)//3+1,1):
        z = (100-5*x-3*y)*3
        if x+y+z==100:
            print('公鸡%d只 母鸡%d只 小鸡%d只'%(x,y,z))
    x=x+1