for x in range(0,20):
    for y in range(0,80):
        if 15*x+9*y+(100-x-y)==300:
            print("公鸡%d只，母鸡%d只，小鸡%d只"%(x,y,100-x-y))