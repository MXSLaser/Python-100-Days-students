a=input('请输入字符串')
b=''
for c in a:
    if c >='a' and c<='z':
        b=b+c.upper()
    elif c>='A' and c<='Z':
        b=b+c.lower()
print(b)