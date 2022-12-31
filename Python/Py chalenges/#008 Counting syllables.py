#Counting syllables
# Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.
# For example, the call count("ho-tel") should return 2.
# def count

def count(str):
    syllables = 1
    for i in range(len(str)):
        if str[i] == '-':
            syllables += 1
    return syllables
print(count('ter-min-a-tor'))