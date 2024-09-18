"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n− 1
"""

def array_dotproduct():
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    # initialize an empty list to store the dot product
    c = []

    # loop through the indices of both arrays
    for i in range(len(a)):
        # multiply the corresponding elements and append them to c
        c.append(a[i] * b[i])
    return c

print(array_dotproduct())
