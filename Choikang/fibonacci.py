list=[1,1]
upper=int(input("请输入你的上限："))
for i in range (0,upper):
    list.append(list[i]+list[i+1])
print("Fibonacci数为")
print(list)