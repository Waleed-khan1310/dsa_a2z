#Functional way

def sumfun(n):
    if n==0:
        return 0
    return n + sumfun(n-1)

print(sumfun(6))
