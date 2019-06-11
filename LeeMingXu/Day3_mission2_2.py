str = input('请输入一串英文：')
str2 = ''

for each in str:
    if each.isupper():
        str2=str2+each.lower()
    elif each.islower:
        str2=str2+each.upper()
print('一个一个字符转换：'+str2)
str3 = str.swapcase()
print('使用内置方法直接一句转换：'+str3)