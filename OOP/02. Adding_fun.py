# In this we are adding some functionality to our class (full_name)
class car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    
    def full_name(self):
        return f"{self.company} {self.model}"
    
s3=car("Toyota","supra")
print(s3.model)
print(s3.full_name())