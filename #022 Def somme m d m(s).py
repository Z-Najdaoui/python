# multi
def multi(a, b):
    result = a * b
    return result

# div
def div(a, b):
    result = a / b
    return result

# somme
def somme(a, b):
    result = a+b
    print(result)

# soustaction
def sous(a, b):
    result = a-b
    print(result)

# enters
a = int(input('Entre Number A: '))
o = input('Enter Opertator(/,*,-,+): ')
b = int(input('Enter Number B: '))

# ifs
if o == '+':
    somme(a, b)
if o == '-':
    sous(a, b)
if o == '/':
    q = div(a, b)
    print(q)
if o == '*':
    w = multi(a, b)
    print(w)
