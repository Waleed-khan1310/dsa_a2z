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