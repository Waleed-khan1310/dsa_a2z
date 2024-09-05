''' 
Pelindrome is a word or number who's reverse is the same as the
orignal number like:- 1331, Radar, Madam
'''

def palin_num(n):

    dup=n
    rev_num=0
    while n>0:
        lastD=n%10
        n=n//10
        rev_num=rev_num*10+lastD
    if rev_num == dup:
        return True
    else:
        return False
    
    
    
print(palin_num(1331))