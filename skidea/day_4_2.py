a=input("输入")
b=''
for ch in a:
    if ch >='F' and ch<='Z':
        ch=chr(ord(ch)-5)
    elif ch>='A' and ch<='E':
        ch=chr(ord(ch)+21)
    b=b+ch
print(b)