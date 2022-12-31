# Min-maxing

# Define a function named largest_difference that takes a list of numbers as its only parameter.

# Your function should compute and return the difference between the largest and smallest number in the list.

# For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

# You may assume that no numbers are smaller or larger than -100 and 100.

'''Type - 1'''
def largest_difference(listNum):
    MinN = min(listNum)
    if MinN < 0:
        return (max(listNum) + MinN)
    return (max(listNum) - MinN)

'''Type - 2'''
def largest_difference(listNum):
    return (max(listNum) - min(listNum))
# print(largest_difference([1,8,-9,10,4,5]))