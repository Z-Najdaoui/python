a = int(input('heur: '))
b = int(input('min: '))

if (a > 23) or (a < 0) or (b > 59) or (b < 0):
    print('Error')
elif (b == 59 and a != 23):
    b = 0
    a = a+1
elif (b == 59 and a == 23):
    b = 0
    a = 0
elif (b == 59):
    b = 0
    a = a+1
    print('The time is', a, ':', b)
else:
    b = b+1
    print('The time is', a, ':', b)
