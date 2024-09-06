'''
Now let's talk about Euclidean algorithms
The Euclidean algorithm is a way to find the greatest common divisor 
of two positive integers.
'''

def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60, 48))