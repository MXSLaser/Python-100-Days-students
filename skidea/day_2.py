import math

radius = float(input('请输入圆的半径: '))
tall = float(input('请输入高度'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
v = area*tall
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
print('体积：%.2f'%v)