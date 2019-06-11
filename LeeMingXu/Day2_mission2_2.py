import math
r = float(input('请输入圆柱的底面半径：'))
h = float(input('请输入圆柱的高；'))
C = math.pi*r*2
Sd = math.pi*r*r
Sc = C*h
St = Sd*2+Sc
V = Sd * h
print('圆柱的底边周长：%.2f' %C)
print('圆柱的底面面积：%.2f' %Sd)
print('圆柱的侧面积：%.2f' %Sc)
print('圆柱的表面积：%.2f' %St)
print('圆柱的体积：%.2f' %V)