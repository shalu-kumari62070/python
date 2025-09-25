class Employee:        # this is basse class
    company = "HCL"
    location = "Lucknow"

    def show(self, name):
        print(f"The name of employee is {name} and your loaction is {self.location}")

        #note = if we write {self.name} then we get error  AttributeError: 'Employee' object has no attribute 'name'
        # for prevent this error we use __init__ otherwise we use uper me jo method hai use

class Programmer(Employee):     # this is derived class
    company = "Info Tech"
    def showLanguage(self, language):
        print(f"the language name is {language}")

a = Employee()
b = Programmer()
a.show("Ram")               # The name of employee is Ram and your loaction is Lucknow
b.showLanguage("pyhton")    # the language name is $pyhton

print(a.company, b.company)   # HCL Info Tech