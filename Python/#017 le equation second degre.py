import math
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))

if a == 0:
    if (not (b == 0)):
        S3 = (-c/b)
        print('le résulta est: S(', S3, ')')
    else:
        print('Math Error')

else:
    delta = (b**2) - (4*a*c)
    print('Delta = ', delta, 'donc:')
    if delta < 0:
        print('inpossible')
    else:
        S1 = ((-b)-(math.sqrt(delta)))/(2*a)
        S2 = ((-b)+(math.sqrt(delta)))/(2*a)
        if S1 == S2:
            print('le résulta est: S(', S1, ')')
        else:
            print('les résultas est: S(', S1, ',', S2, ')')
