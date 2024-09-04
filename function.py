#Creating functin in python
'we can create function in python my "def function_name()"'

def fun():
    print("Here we create our own function, HURRAH!")
fun()

'and we create a function. For printing it we have to call it again like "fun()"'




# now we talk about the parameters 
# A parameter is the variable defined within the parentheses during function definition

def egsum(x,y):
    print(x+y)
egsum(7,8)

""" Here x and y is parameters """    




# Now Argument
# An argument is a value that is passed to a function when it is called. It might be a variable,
# value or object passed to a function or method as input.

def egsum(x,y):
    print(x+y)
egsum(7,10)


def arg_eg(firstname,secondname):
    print(firstname+secondname)
arg_eg("waleed","khan")    

""" Here 7 and 10, waleed and khan are ARGUMENT """




# Here we are writing an example of POSITION ARGUMENT 
""" In the we see the position doesn't matter as long as we diclare in the parameter """

def person_name(first_name,secname):
    print(first_name+secname)
person_name(secname="khan",first_name="Waleed")




""" It is the python function with parameters and argument"""
def sum(firstnum: int, secnum: int):
    jamma=firstnum+secnum
    return(jamma)
firstnum,secnum=10,5
ans= sum(firstnum,secnum)

print(f"the sum of {firstnum} and {secnum} is this {ans}")    




#Now lets create a even odd program with function
def evenodd(x): 
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenodd(int(input("Enter your input: ")))



# Here 

def pass_by_value(b):
    b=b*10
    print("ye to ha bs wahi ha: ", b)
    
pass_by_value(9)




def pass_by_reffermce(list1):
    list1.append('W')
    print('the new list is: ',list1)
    return

my_list=[1,3,5,'waleed']
print('My list before append: ',my_list)
pass_by_reffermce(my_list)


