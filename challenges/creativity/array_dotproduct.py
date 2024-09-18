"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n− 1
"""

def array_dotproduct():
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]

    c = []

    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

print(array_dotproduct())
