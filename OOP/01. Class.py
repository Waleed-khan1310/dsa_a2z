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


# In this we are adding some functionality to our class (full_name)
class car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    
    def full_name(self):
        return f"{self.company} {self.model}"
    
class electriccar(car):
    def __init__(self, company, model, batterySize):
        super().__init__(company, model)
        self.batterySize=batterySize
    
s3=car("Toyota","supra")
print(s3.model)
print(s3.full_name())
my_tesla=electriccar("tesla","model s","1000Kwh")
print(my_tesla.full_name() , my_tesla.batterySize)