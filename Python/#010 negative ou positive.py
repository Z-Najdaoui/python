# <+ ou ->
# var number1,number2,result,signe:float
number1 = int(input('Number 1 :'))
number2 = int(input('Number 2 :'))
result = number1 * number2
if (result >= 0):
    signe = '+'
else:
    signe = '-'
print(signe)
