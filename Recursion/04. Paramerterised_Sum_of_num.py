#Parameterized way
'''
In this approach, instead of using a global variable for calculating the sum, we pass the sum in the 
parameters of the function each time we add an integer to it during the function call.

Here we calculate the sum of natural number with PARAMETERS
'''
def sumNat(n,sum):
    if n<1:
        print(sum)
        return
    sumNat(n-1,sum+n)
    
sumNat(6,0)