lower_limit=int(input('请输入你要找的水仙花数的下限:( >=100 )'))
upeer_limit=int(input('请输入你要找的水仙花数的上限:( <1000 )'))
count=0
for i in range (lower_limit,upeer_limit+1):
     sum=0
     for j in str(i):
         sum+=int(j)*int(j)*int(j)
     if i==sum:
        count+=1
        print('第%d个水仙花数为%d'%(count,sum))