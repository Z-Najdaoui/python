p = int(input('Number of Photocopies you need: '))

if (p < 0):
    s = 'error'
elif (p <= 10):
    s = p*20
elif (p > 10 and p <= 30):
    s = 10*20+(p-10)*15
elif (p > 30):
    s = 10*20+20*15+(p-30)*10
if (isinstance(s, str)):
    print(s)
else:
    print('prix est: ', s, 'Rial')
