"""
Create Phone Number
6kyu

Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => returns "(123) 456-7890"

"""
# Version 1
def create_phone_number(n):
    # Your code goes here
    n = str(n)
    phone_number = '('
    for i, num in enumerate(n) :
        if i < 3:
            phone_number += str(num)
            if i == 2:
                phone_number += ')'
                phone_number += ' '
        elif i < 14 and i > 2:
            phone_number += str(num)
            if i == 5:
                phone_number += '-'               
    return phone_number
    
 # Version 2
 def create_phone_number_ver2(n):
    # Your code goes here
    n = str(n)
    phone_number = '('
    for i in range(10) :
        if i < 3:
            phone_number += n[i]
            if i == 2:
                phone_number += ')'
                phone_number += ' '
        elif i < 10 and i > 2:
            phone_number += n[i]
            if i == 5:
                phone_number += '-'               
    return phone_number
