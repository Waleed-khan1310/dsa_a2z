# Let's create a pass statement 
# In the the program will not execute 

a=4
b=6

""" 
Here see this while statement is wrong but i didn't give an error because
of pass statement it is ignored
"""
while a==3 or b==3:
    a+=1
    b+=2
    pass

sum=a+b
print(sum)