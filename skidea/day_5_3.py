'''
我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
输入：
输出：
0 25 75
4 18 78
8 11 81
12 4 84
'''
m=0
while m<=100//5:
    for f in range(0,100//3):
        if (m*5+f*3+(100-m-f)/3)==100:
            print(m,f,(100-m-f))
    m=m+1