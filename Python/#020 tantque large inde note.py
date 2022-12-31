from ast import If


ma = int(input('-Note 1:'))
if (ma == 0):
    print('-There is no notes.')
else:
    indema = 1
    i = 2
    s = ma
    while not (s == 0):
        s = int(input('-Note '+str(i)+':'))
        if s > ma and not (s == 0):
            ma = s
            indema = i
        i += 1
    print('\n waiting . . .\n')
    print(' The biger Note is: ', ma, ', in inde Number: \
\"', indema, '\"', sep="")
