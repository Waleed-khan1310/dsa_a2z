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