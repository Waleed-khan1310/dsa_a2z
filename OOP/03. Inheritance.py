# Here electriccar inherits form car class
class car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    
    def full_name(self):
        return f"{self.company} {self.model}"
    
class electriccar(car):
    def __init__(self, company, model, batterySize):
# Super is a keyword to access attributes from the pervious class
        super().__init__(company, model)
        self.batterySize=batterySize
    
my_tesla=electriccar("tesla","model s","1000Kwh")
print(my_tesla.full_name() , my_tesla.batterySize)