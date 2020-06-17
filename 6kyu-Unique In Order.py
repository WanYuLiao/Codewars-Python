"""
Unique In Order
6kyu

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
# Version 1
def unique_in_order(iterable):
    
    length = len(iterable)
    unique = [iterable[0]]
    for i in range(length-1):
        if iterable[i]== iterable[i+1]:
            i = i
        else:
            unique += iterable[i+1]
    return unique

# Version 2
def unique_in_order(iterable):
    result = []
    for i in range (len(iterable)-1):
        if iterable[i] != iterable[i+1]:
            result += iterable[i]
    if iterable[:] != iterable[len(iterable)-1]:
        result += iterable[-1]
    return result

# Test Run
print(unique_in_order('aabbccdedd'))
print (unique_in_order('aabccdeeaa'))
