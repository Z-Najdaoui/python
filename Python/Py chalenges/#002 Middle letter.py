def mid(str):
    n = len(str)
    print(str)
    print(n)
    if n%2 == 0:
        return ""
    index = int((n-1)/2)
    return str[index]
print(mid('abc'))
