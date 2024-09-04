# Lets create a for_loop for string

loopeg='Waleed Khan'
for i in loopeg:
    print(i)
    
    
    
# Now lets create a for_loop for range of numbers

listeg=[1,2,3,4,5,6]
for i in listeg:
    print(i,end=" ")
    
# Another

print('\n')
for i in range(0,99,3):
    print(i,end=' ')

''' Here 0 is the starting point, 99 is the max point but 99 itself not include, 3 is how difference gap we want'''



# Python_for_loop Enumerate
# Tell us the index and as well as the input
print('\n')
list1=['waleed', 'khan', 3,4,5,'AI']
for count,ele in enumerate(list1):
    print(count,ele)
    
    
    
# Nested for_loop

for i in range(1,5):
    for k in range(1,5):
        print('\n',i,k)
        
        
        
# Python For_loop over list

list1=['Waleed','Khan','Family']
for i in list1:
    for k in list1:
        print(i,k)
        
        
        
# For_loop in one line 
# It prints numbers in list

exlis=[k for k in range(26)]
print(exlis)
    
    
    
# For_loop with Dictionary
d=dict()
d["Waleed"]=123
d['Khan']=456
for i in d:
    print('%s %d' % (i,d[i]))



# Python for_loop with tuple
tuex=(('tuple',15),("for_loop",1122))
for a,b in tuex:
    print(a,b)



# Python for_loop with Zip function
fruit=['Apple','banana','Guava']
color=['Red','Yellow','Green']
for fruit,color in zip(fruit,color):
    print(fruit,'is',color)



# Continure in Python for_loop
''' It print all the letters except the give letter (l,5,e) '''

eg=(1,3,5,2,'waleed')
for i in eg:
    if i=='l'or i==5 or i=='e':
        continue
    print('current letter is: ',i)    
    
''' Another example '''

eg=('waleed')
for i in eg:
    if i=='l' or i=='e':
        continue
    print('current letter is: ',i)    
     
     
     
# Break in Python for_loop
''' Whenever program see that l or 3 or e it break the program and give us the output '''

eg=[1,3,5,2,'waleed']
for i in eg:
    if i=='l'or i==3 or i=='e':
        break
    print('current letter is: ',i)    



# For Loop in Python with Pass Statement
''' It prints only last letter of the given word '''

for i in "waleed khan":
    pass
print('Last letter is: ',i)       



# Else statement in for_loop 
for i in range(1,9):
    print('Here your numbers: ',i)
else:
    print('Heres the example of this.')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    