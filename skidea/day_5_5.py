"""
Craps赌博游戏
玩家掷两个骰子，点数为1到6
如果第一次点数和为7或11，则玩家胜
如果点数和为2、3或12，则玩家输，
如果和 为其它点数，则记录第一次的点数和，
然后继续掷骰，直至点数和等于第一次掷出的点数和，则玩家胜
             如果在这之前掷出了点数和为7，则玩家输。
             输入输出略030
"""
from random import randint
#while True:
a=randint(1,6)
b=randint(1,6)
print(a+b)
if a+b==7 or a+b==11:
    print('you win!!!')
elif a+b==2 or a+b==3 or a+b == 12:
    print ('you lost....')
else:
    while True:
        c = randint(1, 6)
        d = randint(1, 6)
        print(c+d)
        if c+d==a+b:
            print('you win!!!')
            break
        if c+d==7:
            print('you lost....')
            break
