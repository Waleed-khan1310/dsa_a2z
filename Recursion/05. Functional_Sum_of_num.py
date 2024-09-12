#Functional way

def sumfun(n):
    if n==0:
        return 0
    return n + sumfun(n-1)

print(sumfun(6))


# Code for sum of num with the power of 3 i.e:- 1**3 + 2**3 + 4**3 =36
def sumnum(n):
    if n==0:
        return
    return (n * (n+1)//2)**2
print(sumnum(5))
