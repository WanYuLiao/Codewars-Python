"""
Is this a triangle? Ver.1
7kyu

Implement a method that accepts 3 integer values a, b, c. 
The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""
# Version 1
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <=0:
        return False
    max_side = max(a,b,c)
    if max_side >= a + b + c - max_side:
        return False
    else:
        return True

# Version 2
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

# Test Run
print (is_triangle(7,2,2))
print (is_triangle(4,3,2))
