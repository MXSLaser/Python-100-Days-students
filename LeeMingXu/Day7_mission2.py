for i in range(1,10):
    print('      '*(9-i),end="")
    for j in range(1,i+1):
        print("{0} * {1} = {2}".format(j,i,i*j),end="   ")
    print()