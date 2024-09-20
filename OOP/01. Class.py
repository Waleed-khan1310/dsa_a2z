class student:
# Here we are creating a class with name student
    def __init__(self,name,num):
        self.name=name
        self.rollnum=num
        
s1=student('waleed',98)
print(s1.name)
print(s1.rollnum)

s2=student('Arif',97)
print(s2.rollnum)