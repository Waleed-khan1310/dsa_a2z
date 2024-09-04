# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false, the line immediately after the loop in the program is executed.
''' 
Python for loop is usually used when the number of iterations is known, whereas Python while loop is used 
when the number of iterations is unknown

'''


egnum=3
while(egnum<9):
    egnum=egnum+2
    print('Waleed Khan')
print('Hello.')


# Continue While_loop
# It print all the letter except the one we are giving it

a=0
b= 'ArtificialoIntelligenceq'
while a<len(b):
    if b[a]=='o' or b[a]=='q':
        a+=1
        continue
    print(b[a],end='')
    a+=1
    
    
    
# Continue statement in while_loop

a=0
b=4

while(a<=15):
    if a==11 or a==14:
        print('We skip this iteration.')
        a+=1
        continue
    c=b*a
    print(b, 'X', a, '=',c)
    a+=1



# Break statement in While_loop

fnum=0
snum=5

while(fnum<=20):
    if fnum==14 or fnum==16:
        print('The statement is break it is equal to', fnum)
        break
    multiple=snum*fnum
    print(snum, "X" , fnum, '=', multiple)
    fnum+=1
    
    
    
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



# Sentinel Controlled Statement
# In this we chose a specific num to end the program

a=int(input('Give any num to continue and -1 to end the program: '))
while a!=1:
    a=int(input('Give any num to continue and -1 to end the program: '))
    
         

    