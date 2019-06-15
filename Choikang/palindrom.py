def palindrom(num):
    if len(num)<2:
        return True
    if num[0]==num[-1]:
        return palindrom(num[1:-1])
    else :
        return False
if __name__ == '__main__':
    num=input("请输入一串字符串：")
    print(palindrom(num))