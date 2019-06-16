def isprime(year):
    if year%4==0 and year%100!=0 or year%400==0 :
        return True
    else:
        return False
if __name__ == '__main__':
    primeMonth=[31,29,31,30,31,30,31,31,30,31,30,31]
    NprimeMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    start =input().split(' ')
    end = input().split(' ')
    startday=[int(start[0]),int(start[1]),int(start[2])]
    endday = [int(end[0]),int(end[1]),int(end[2])]
    tmp=0
    tmpSM=0
    tmpEM=0
    for i in range(startday[0]+1,endday[0]):
        if isprime(i):
            tmp+=366
        else:
            tmp += 365
    for i in range(0,startday[1]-1):
        if isprime(startday[0]) :
            tmpSM+=primeMonth[i]
        else:
            tmpSM+=NprimeMonth[i]
    for i in range(0,endday[1]-1):
        if isprime(endday[0]) :
            tmpEM+=primeMonth[i]
        else:
            tmpEM+=NprimeMonth[i]
    if isprime(endday[0]):
        tmpS=366
    else:
        tmpS=365
    if startday[0]== endday[0]:
        date =tmpEM+endday[2]-tmpSM-startday[2]
    elif startday[0]!=endday[0]:
        date =tmp+tmpEM+endday[2]-tmpSM-startday[2]+tmpS
    print(date)