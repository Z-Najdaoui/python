# < gives you next 10 doubles numbers after N >

N = input('Number:')
listN = list(N)

# if number(N) double
if listN[-1] in {'0', '2', '4', '6', '8'}:
    N = int(N)
    for i in range(N, (N + 20), 2):
        print(i)

# if number(N) single
else:
    N = int(N)
    N = N + 1
    for i in range(N, (N + 20), 2):
        print(i)

print(listN)
