#function that find the big divion number between two numbers
def grandDiv(a, b):
    #make the bigger volume in a
    if b > a: 
        c = b
        b = a
        a = c

    #Euclidean algo
    while True:
        mod = a % b
        if mod == 0:
            print(b)
            break
        a = b
        b = mod

#Inputs Number
while True:
    num1 = int(input('num 1: '))
    if num1 > 0:
        break
while True:
    num2 = int(input('num 2: '))
    if num2 > 0:
        break
#Call function
grandDiv(num1, num2)