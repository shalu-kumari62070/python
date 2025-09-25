class Employee:

    # getter using @property
    @property
    def name(self):
        return self.name
    
    # setter using @name.setter
    @name.setter
    def name(self,value):
        self.fname = value
    
e = Employee()

e.name = "Hary khan"
print(e.name)