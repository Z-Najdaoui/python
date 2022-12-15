def myFun(n):
    return lambda r: n * r
y = int(input("num: "))
times = myFun(y)
for i in range(1,11):
    print(times(i))