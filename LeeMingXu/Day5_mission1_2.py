'''
测试问题2：寻找“完美数”
输入：1000 5
预计输出：6, 28, 496
'''
import math
print('寻找“完美数”')
numup = input('请输入范围上限:')
numlow = input('请输入范围下限:')
if int(numlow)>int(numup):
    print('范围非法')
    exit();
for i in range(int(numlow),int(numup)+1,1):
    sum = -i
    if(i==1):
        sum = -2
    for j in range(1,int(math.sqrt(i))+1,1):
        if i % j == 0:
            sum = sum + j + (i / j)
    if sum == i:
        print(' ' + str(i) + ' ')