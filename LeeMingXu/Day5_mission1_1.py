'''
测试问题1：寻找“水仙花数”
输入：999 100
预计输出：153，370，371，407
'''
print('寻找“水仙花数”(100-999)')
numup = input('请输入范围上限:')
if int(numup)>999:
    print('范围超限')
    exit();
numlow = input('请输入范围下限:')
if int(numlow)<100:
    print('范围超限')
    exit();
if int(numlow)>int(numup):
    print('范围非法')
    exit();
for i in range(int(numlow),int(numup)+1,1):
    ls = list(str(i))
    sum = 0
    for j in ls:
        sum = sum + int(j) * int(j) * int(j)
    if sum == i:
        print(' ' + str(i) + ' ')