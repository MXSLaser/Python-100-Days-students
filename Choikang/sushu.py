def sushu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    if (n>=i):
        return True
def zhen(num):
    mun=''
    j=1
    for i in num:
        mun = mun+num[-j]
        j+=1
    if sushu(int(num)) and sushu(int(mun)):
        print('yes')
    else:
        print ('no')
if __name__ == '__main__':
    n=str(input("请输入你要输入的数字"))
    print(zhen(n))