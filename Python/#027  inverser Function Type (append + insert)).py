
def inverser(Tableu):
    anotherT = []

    # append
    for i in range(len(Tableu)-1,-1,-1):
        anotherT.append(Tableu[i])

    # Insert
    # for i in range(0, len(Tableu)):
    #     anotherT.insert(0, Tableu[i])

    return anotherT


tableu = []
e = 0
print('enter \'s\' for stop!')
while True:
    arrs = input('Enter T['+str(e)+'] : ')
    if arrs == 's':
        break
    arrs = int(arrs)
    tableu.append(arrs)
    e += 1
print(inverser(tableu))
