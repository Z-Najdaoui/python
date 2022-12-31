def double_letters(str):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            return True
    return False
print(double_letters("slfajhh"))