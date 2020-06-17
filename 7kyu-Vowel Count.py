"""
Vowel Count
7kyu

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""
# Version 1
def get_count(input_str):
    num_vowels = 0
    string = list(input_str)
    for i in range (len(string)):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            num_vowels += 1
    return num_vowels

# Version 2
def getCount(s):
    return sum(c in 'aeiouAEIOU' for c in s)

# Test Run
print (get_count('abcde'))
print (getCount('abcdeABCDE'))
