Day = input('请输入年月日：')
year = int(Day.split(' ')[0])
month = int(Day.split(' ')[1])
day = int(Day.split(' ')[2])
days = day
for i in range(1,month):
    if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        days+=31
    elif i==4 or i==4 or i==9 or i==11:
        days+=30
    elif i==2 and ((year%4==0 and year%100!=0) or year%400==0):
        days+=29
    else:
        days+=28
print(days)