# Python function with parameters and argument
def sum(firstnum: int, secnum: int):
    jamma=firstnum+secnum
    return(jamma)
firstnum,secnum=10,5
ans= sum(firstnum,secnum)

print(f"the sum of {firstnum} and {secnum} is this {ans}")    




# Immutable object shows Pass_by_value
def pass_by_value(b):
    b=b*10
    print("ye to ha bs wahi ha: ", b)
    
pass_by_value(9)



# Mutable object shows Pass_by_reference
def pass_by_reffermce(list1):
    list1.append('W')
    print('the new list is: ',list1)
    return

my_list=[1,3,5,'waleed']
print('My list before append: ',my_list)
pass_by_reffermce(my_list)