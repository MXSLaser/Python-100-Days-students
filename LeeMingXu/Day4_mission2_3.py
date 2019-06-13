str = input('请输入密文：')
ls = list(str)
for i in range(len(ls)):
    if 'A'<=ls[i]<='E':
        print('%c'%(ord(ls[i])+21))
        ls[i] = chr(ord(ls[i])+21)
    elif 'F'<=ls[i]<='Z':
        print('%c'%(ord(ls[i])-5))
        ls[i] = chr(ord(ls[i])-5)
str = ''.join(ls)
print('明文为：'+str)