"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列
因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上
斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）在现代物理、准晶体结构、化学等领域
斐波纳契数列都有直接的应用
输入： 10
输出： [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
number=input("请输入需要个数")
number=int(number)
a=[]
a.append(1)
a.append(1)
num=2
i=2
while number>=num:
    a.append(a[i-1]+a[i-2])
    i=i+1
    num=num+1
if(number==1):
    print('1')
else:
    print(a)