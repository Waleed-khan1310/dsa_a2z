#Driving factorial of a number with recursion
def factor(n):
    if n<1:
        return 1
    print(n, end=' ')
    return n*factor(n-1)
print(factor(6))


