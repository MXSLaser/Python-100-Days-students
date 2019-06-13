'''
测试问题5：骰子赌博游戏
规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
输入：1000
预计输出：具有随机性，无法预测  
'''
from random import randint
import os
money = int(input('请输入您带入的资金数目：'))
print('您当前剩余资金：%d'%(int(money)))
dz = input('请下注：')
first = randint(1,6)+randint(1,6)
print('结果为：%s'%(first))
if first == 7 or first == 11:
    print('玩家获胜')
    os.system('pause')
elif first == 2 or first == 3 or first == 12:
    print('庄家获胜')
    os.system('pause')
else:
    money = money - int(dz)
    print('游戏继续')
    os.system('pause')
    while money>0:
        os.system('cls')
        print('您当前剩余资金：%d'%(int(money)))
        dz = input('请下注')
        if money - int(dz) < 0:
            print('您的剩余资金不足')
            os.system('pause')
            continue
        elif money-int(dz)==0:
            print('您的资金可能不足以支持下一次赌博')
        result = randint(1,6)+randint(1,6)
        print('结果为：%s'%(result))
        if result == first:
            print('玩家获胜')
            os.system('pause')
            break
        elif result == 7:
            print('庄家获胜')
            os.system('pause')
            break
        else:
            money = money - int(dz)
            print('游戏继续')
            os.system('pause')