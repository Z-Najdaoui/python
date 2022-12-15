def estPremier(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


def extraireNbrsPremier(x):
    for i in range(2, x+1):
        if (estPremier(i) == True):
            print(i, end="|")


def nextPremier(num):

    while True:
        num += 1
        if estPremier(num):
            print('\nThe next premier est: ', num)
            break


while True:
    x = int(input("x="))
    if (x > 1):
        break
if (estPremier(x) == True):
    print(x, " est premeir")
else:
    print(x, "n'est pas premeir")
extraireNbrsPremier(x)
nextPremier(x)
