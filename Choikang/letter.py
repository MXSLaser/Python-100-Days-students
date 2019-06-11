str=input('请输入一个字符串：')
STR=''

for x in str:
    if x.isupper():
        STR+=x.lower()
    else:
        STR+=x.upper()
print('将大小写转变后的字符串为：'+STR)