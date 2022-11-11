# funciton for get number of vowiels in string(str)
def myFun(str):
    sum = 0
    str = list(str)

    for i in range(0, len(str)):
        if str[i] in {'e', 'a', 'u', 'i', 'o'}:
            sum += 1

    print('\nThe number of vowels in this text is: ', sum)


#Input string
string = input('Enter text here: ')

# call function
myFun(string)
