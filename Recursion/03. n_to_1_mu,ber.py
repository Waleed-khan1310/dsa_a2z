#Printing n to 1 numbers
def recfun3(n):
    if n==0:
        return
    print(n)
    recfun3(n-1)
    

recfun3(7)