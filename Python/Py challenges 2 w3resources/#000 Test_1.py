def get_sum(a,b):
    if a>b:
        times = a - b
        theSmallNumber = b
    else:
        theSmallNumber = a
        times = b-a
    sum = 0
    for i in range(times+1):
        sum += (theSmallNumber+i)
    return sum
print(get_sum(3,3))