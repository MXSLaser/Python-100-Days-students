def sushu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    if (n>=i):
        return True
def palindrom(num):
    if len(num)<2:
        return True
    if num[0]==num[-1]:
        return palindrom(num[1:-1])
    else :
        return False
if __name__ == '__main__':
    num = input("请输入一串字符串：")
    if sushu(int(num)) and palindrom(num):
        print("True")
    else:
        print("False")