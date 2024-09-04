#Types if Conditional Statement
"""
1.Python If Statement
2.Python If Else Statement
3.Python Nested If Statement
4.Python Elif
5.Ternary Statement | Short Hand If Else Statement

"""
#lets creat a if statement

if_eg=20

if if_eg>15:
    print("your statement is true, YASSS!")
print("your statement is false, NAHHHH")


#lets create a if_else statement 

ifelse_eg=13

if ifelse_eg<=10:
    print("your statement is true, good for you")
    print("yes i am in if statement")
else:
    print("no i am not in if statement")
    print('your statement is false')
print('Good work WALEED you are doing great')


# Nested if statement is defined as 'if statement with in the if statement'
# now lets create the nested if statement

nif_eg=9
if(nif_eg==9):
    print("Dekho")
    
    if(nif_eg<15):
        print("Laga Raha Waleed")
        
    if(nif_eg>11):
        print("Ye to ni hona")
    else:
        print("I hope you enjoy")

print("Ye to yahi ruk jae ga")

# lets create elif statement
# Elif statement only execute one statement which is true other will be ignored

lif=9
if(lif==10):
    print("your output is equal to 10")

elif(lif<8):
    print("your output is smaller then 8")
    
elif(lif>5):
    print("your output is larger then 5")
    
else:
    print("non of your statement is true")                            
        

