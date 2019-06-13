password=input('请输入你的密文：')
PASSWORD=''
for i in password:
    if 65<=ord(i)<70:
        PASSWORD+=chr(ord(i)+21)
    elif 70<=ord(i)<=90:
        PASSWORD+=chr(ord(i)-5)
    else:
        PASSWORD+=i
print('修改后的明文为：'+PASSWORD)

