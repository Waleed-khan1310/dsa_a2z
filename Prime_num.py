'''
Prime number is a number which has 2 factors (1 and itself)
ONE IS NOT A PRIME NUMBER BECAUSE IT HAS ONLY ONE FACTOR.
'''

def isprime(n):
    count=0
    for i in range(1, n+1):
        if n%i==0:
            print(i)
            count=count+1
    if count==2:
        return "prime number"
    else:
        return'not prime number'
    
print(isprime(7))