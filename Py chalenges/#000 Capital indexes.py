def capital_indexes(str):
    capitals = []
    for i in range(len(str)):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
         capitals.append(i)
    return capitals
# print(capital_indexes('dkfjdfHHdkjfdkjfBBBdkljfkdjfdkjfuuuVIO'))