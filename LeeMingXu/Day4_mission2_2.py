n = 0
h = 0.0001
while h <= 8848:
    n = n + 1
    h = h * 2
print('一共折了%d次,最后厚度为%f' %(n,h))