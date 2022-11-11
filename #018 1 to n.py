n = int(input('n'))
S1 = 0
S2 = 0
for i in range(1, n+1):
    S1 = S1+(1/i)
print(S1)
for i in range(n, 0, -1):
    S2 = S2+(1/i)
print(S2)
print('Donc: 1 a n egal n a 1')
