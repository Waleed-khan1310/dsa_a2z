'''
 Armstrong number is a number that is equal to the sum of its own 
 digits each raised to the power of the number of digits.
'''

def arm_num(n):
    dup = n
    len_n=len(str(n))
    sum = 0
    while n>0:
        lastD=n%10
        sum= sum + (lastD**len_n)
        n=n//10
    if sum == dup:
        return True
    else:
        return False


print(arm_num(371))