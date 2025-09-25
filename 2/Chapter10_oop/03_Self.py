class Employee:
    language = "python"   # this is class attribute 
    salary = 12000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # note = if we write getInfo() then it gives error

    def greet(self):
        print("good morning")

a = Employee()
a.getInfo()  # a.getInfo is converted into Employee.getInfo(a)
# if we does not write self in getInfo() this gives error
a.greet()

# output
# The language is python. The salary is 12000
# good morning