##Python code give's ansawer "yes" if the num1,num2 'premiers entre eux' "no" for else

def premiers(a, b):
    #make the bigger volume in a
    if b > a: 
        c = b
        b = a
        a = c

    #Euclidean algo
    while True:
        mod = a % b
        if mod == 0:
            print('\npremiers entre eux : ' ,end='')
            if b==1: ## premiers entre eux ?
                print('Yes')
            else:
                print('No')    
            break
        a = b
        b = mod

#Inputs Number
while True:
    num1 = int(input('Enter the first number : '))
    if num1 > 0:
        break
while True:
    num2 = int(input('Enter the second number : '))
    if num2 > 0:
        break
#Call function
premiers(num1, num2)