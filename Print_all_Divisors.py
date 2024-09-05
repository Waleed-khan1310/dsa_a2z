'''
In this wwe find that on what numbers our number divide properly that 
it's reminder is 0
'''


num=int(input('Enter number:'))
for i in range(1, num + 1):
    if num % i ==0:
        print(i)
    
    
    
    

num2=6
i=1
while i<=num2:
    if num2%i==0:
        print(i, end='')
    i=i+1