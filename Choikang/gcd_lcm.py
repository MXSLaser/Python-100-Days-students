def gcd(m,n):
    if m<n:
        m,n=n,m
    while n!=0:
        r=m%n
        m=n
        n=r
    return m
def lcm(m,n):
    result=0
    while 1:
        result = result + 1
        if (result % m == 0 and result % n == 0):
            break
    return result
if __name__ == '__main__':
    m=int(input("请输入第一个数："))
    n=int(input("请输入第二个数："))
    print("两数的最大公约数为%d" % gcd(m, n))
    print("两数的最小公倍数为%d" % lcm(m, n))


