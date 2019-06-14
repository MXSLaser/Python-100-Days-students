from random import randint
money=int(input('请输入您带的总资金：'))
print('您当前剩余资金：%d'%(int(money)))
x = input('请下注：')
first = randint(1,6)+randint(1,6)
print('结果为：%d'%(first))
if first == 7 or first == 11:
    print('玩家获胜,游戏结束')
    exit()
elif first == 2 or first == 3 or first == 12:
    print('庄家获胜，游戏结束')
    exit()
else:
    money = money - int(x)
    print('游戏继续')
    while money>0:
        print('您当前剩余资金：%d'%(money))
        x= input('请下注')
        if money - int(x) < 0:
            print('您的资金不足下注')
            continue
        other = randint(1,6)+randint(1,6)
        print('结果为：%d'%(other))
        if other == first:
            print('玩家获胜')
            break
        elif other == 7:
            print('庄家获胜')
            break
        else:
            money = money - int(x)
            print('游戏继续')