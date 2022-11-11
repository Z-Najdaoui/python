##min+1


H = int(input('Heur: '))
M = int(input('Min: '))
if (H > 23) or (H < 0) or (M > 59) or (M < 0):
    print('Incorect Time')
M = M+1
if (M == 60):
    M = 0
    H = H+1
if (H == 24):
    H = 0
print(H, ':', M)
