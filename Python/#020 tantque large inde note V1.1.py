a = int(input('Entre number 1 :'))
max = a
indecmax=1
i=2

while not (a == 0):
    a = float(input('Entre number'+str(i)+':'))
    if (max<=a):
        max = a
        indecmax = i
    i=i+1

print(max,indecmax)