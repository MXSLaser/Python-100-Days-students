import math

radius = float(input('请输入底圆的半径: '))
h=float(input('请输入圆柱的高度:'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
V=area*h
print('底圆的周长: %.2f' % perimeter)
print('底圆的面积: %.2f' % area)
print('体积: %.2f' % V)
