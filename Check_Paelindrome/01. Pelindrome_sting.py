'''
In the previous example we check palindrome of the integer num, Now 
let's check with the sting
'''

def palin_sting(n):
    dup2=n
    n=n[::-1]
    if n==dup2:
        return True
    else:
        return False
    
    
print(palin_sting('waleed'))