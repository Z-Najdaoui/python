import math
# 1. Write a Python program to check if a given positive integer is a power of two.
# Input : 4
# Output : True

def isSquare(num):
    if num<0:
        return False
    return math.sqrt(num) % 1 == 0
print(isSquare(-9))