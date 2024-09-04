#Data types:-
            #numeric
                  #int
                  #float
                  #complex
            #boolean
            #sequence type
                   #string
                   #tuple
                   #list
            #Set
            #dictionary 
            #Binary Type



#Find data type by writing "type()"

a='waleed'
print('type of a is: ', type(a))

a="waleed"
b=True
c=123
d=1.5

print(type(a))
print(type(b))
print(type(c))
print(type(d))



#Accessing single single letter in a string

b="my name is waleed"
print("printing whole string:", '\n' , b)
print('print fourth letter of the string: ', '\n', b[4])


#Creating List
list_eg=['waleed','khan','good','coder']
print(list_eg)
print(list_eg[2])     


#to add something the list we use a function  variable_name.append(thing we want to add)
#to remove something the list we use a function  variable_name.remove(thing we want to remove)
listeg2=['waleeds','khans','good','coders','family']
listeg2.remove("good")
print(listeg2)     
listeg2.append("HURRAH!")               
print(listeg2)
                     
           
                       
#creating tuple



tuple2=('waleed','geek')
print(tuple2)     

Tuple1=tuple('waleed')
print(Tuple1)       


print(Tuple1,tuple2)

Creating_eg=(tuple2,Tuple1)
print(Creating_eg)



'WALEED YOU ARE WEAK IN LIST, TUPLE GO STUDY IT'




#SET data type


'creating a mix list and string data type in set'

set_list=set(['muhammad','waleed','khan','1','57','waleed'])
print(set_list)


'we cannot find the index in the set but we find wether the number is in the set are not ny using "i" function '


set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)
print("\nElements of set: ")


for i in set1:
    print(i, end=" ")
'HERE i IS THE INDEX LIKE (0,1,2,3...)'   


print("Geeks" in set1)
'HERE WE ARE DOING THAT THE GREEK ARE AVAIBLE IN THE SET OR NOT AND IT IS PRESENT SO IT RETURN TRUE '




#creating dictionary

dic_eg= {2:'waleed','family':'happy',1:6,5:[1,3,5,7,8]}
print(dic_eg)






age_input=input("enter your age;")
input=int(age_input)
if age<0:
print("enter correct age.")
elif age < 18:
print("you are minor.")
elif age >= 18 and age > 65:
print("you are adult.")
else 
print("you are are senior citizen.")