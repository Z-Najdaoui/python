N = int(input('Enter the number N: '))
print('\n')
for I in range(1, N+1):
    for sn in range(1, 5):
        inputsn = int(input('Enter The Number '+str(sn)+' en N'+str(I)+': '))
        if sn == 1:
            minsn = inputsn
            maxsn = inputsn
        if inputsn > maxsn:
            maxsn = inputsn
        if inputsn < minsn:
            minsn = inputsn
    print('\nThe large Number en N', I, 'Is', maxsn)
    print('The small Number en N', I, 'Is', minsn)
    print('\n')

    if I == 1:
        maxN = maxsn
        minN = minsn
    if maxN < maxsn:
        maxN = maxsn
    if minN > minsn:
        minN = minsn
print('\nThe large Number in All Ns is ', maxN)
print('The small Number in All Ns is ', minN)
