# Anagrams

# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(str1,str2):
    if not(len(str1)==len(str2)):
        return False
    for i in range(len(str1)):
        if not(str1.count(str2[i])):
            return False
        if not(str1.count(str1[i]) == str2.count(str1[i])) or not(str2.count(str2[i]) == str1.count(str2[i])):
            return False
    return True
# print(is_anagram('ABBA','AABB'))
