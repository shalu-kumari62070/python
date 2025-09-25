class Employee:
    language = "python"   # this is class attribute 
    salary = 12000

    def __init__(self):  # It is dunder method which is call automatically
        print(" i am creating an object")

    def greet(self):
        print("good morning")


a = Employee()  
# output
# i am creating an object

# next example
class learn:
    language = "python"   # this is class attribute 
    salary = 12000

    def __init__(self, name, language, salary):  # It is dunder method which is call automatically
        self.name = name
        self.language = language
        self.salary = salary


b = learn("code", "javascript", 18000)
print(b.name, b.language, b.salary)  # code javascript 18000
