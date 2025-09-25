class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100



e = Employee()
# print(e.salaryAfterIncrement)  # 46800.0
e.salaryAfterIncrement = 280.8
print(e.increment)   # 19.999999999999996

