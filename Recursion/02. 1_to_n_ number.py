#Printing 1 to n numbers
def recfun2(n):
    if n==0:
        return
    recfun2(n-1)
    print(n, end='')
recfun2(5)