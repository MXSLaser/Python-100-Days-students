upper_limit=int(input('请输入你要找的完全数的上限:'))
count=0
for i in range (2,upper_limit):
    L=[]
    for j in range(1,i):
        if i%j==0:
            L.append(j)
    if sum(L)==i:
        count=count+1
        print('第%d个完全数为%d：'%(count,i))
