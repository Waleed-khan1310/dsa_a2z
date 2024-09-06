'''
In this wwe find that on what numbers our number divide properly that 
it's reminder is 0
'''


num=int(input('Enter number:'))
for i in range(1, num + 1):
    if num % i ==0:
        print(i)
    
    
    
    
# With while loop
num2=6
i=1
while i<=num2:
    if num2%i==0:
        print(i)
    i=i+1

    
    
# In this we done it with the help of square root which is more optimal
# way to do it
import math as m
output_list=[]
n=36
for i in range(1,int(m.sqrt(n))):
    if n%i==0:
        output_list.append(int(i))
        if n//i !=1:
            output_list.append(int(n/i))
output_list.sort()
print(output_list)



# Here we make a function
import math as m
def divisor(n):
    output_list2=[]
    
    for i in range(1,int(m.sqrt(n))):
        if n%i==0:
            output_list2.append(int(i))
            if n//i !=i:
                output_list2.append(int(n/i))
    output_list2.sort()
    return output_list2
    

print(divisor(36))