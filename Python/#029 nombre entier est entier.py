while True:
    num = int(input('Enter the number:'))
    if num>0:
        break
a=0
print('__________________\n')
print('Number',num,' premier :' ,end=' ')
for i in range(2,num):
    d = num/i
    if d%1 == 0:
        a=-1
        print('No, Because',num,'/',i,'=',num/i)
        break
if a==0:
    print('Yes')
print('__________________')
    