def namefun(fname='Muhammad', Sname='Waleed', Lname='Khan'):
    print(fname,Sname,Lname)


namefun('Muhammad','Arif', 'Mughal')



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



# Finding duplicate letter

c=['waleed',1,2,3,2,1,'waleed','khan']
duplicate=None
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i]==c[j]:
            duplicate = c[i]
            print(duplicate)
        
        
        
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
sum=a*b
print(f'The product of {a} and {b} is: ', sum)





