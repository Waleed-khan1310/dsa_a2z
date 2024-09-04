''' 
In this code we countin the the input number 
'''
n=987654
while n>0:
    lastD=n%10
    n=n//10
    print(lastD)
    
    
    
    
''' 
Now let's write a code of reversing a number
'''    
    
a=987654321
reverd=0
while a>0:
    akhri_num=a%10
    a=a//10
    reverd=reverd*10+akhri_num
print(reverd)








a=987654321
reverd=0
dublicate=a
while a>0:
    akhri_num=a%10
    a=a//10
    reverd=reverd*10+akhri_num
print(reverd)

if reverd==dublicate:
    print("true")
