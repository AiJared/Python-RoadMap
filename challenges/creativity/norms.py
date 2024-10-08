"""
The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as
v = p v1p + v2p + ··· + vnp.
For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. 
For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of √42 + 32 = √16+ 9 = √25 = 5. 
Give an implementation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
"""

def norm(v, p=2):
    # Compute the p-norm is p is provided
    return sum(abs(x) ** p for x in v) ** (1/p)

v = [4, 3]
print(norm(v))      # Euclidean norm (default p=2)
print(norm(v, 3))   # p-norm for p = 3