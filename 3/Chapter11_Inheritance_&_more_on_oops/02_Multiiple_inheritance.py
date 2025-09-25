class Employee:        # this is basse class
    company = "HCL"
    location = "Lucknow"

    def show(self, name):
        print(f"The name of employee is {name}")

class Coder:
    language ="Python"
    def printLanguage(self):
        print(f"out of all the language here is your language {self.language}")

class Programmer(Employee, Coder):     # this is derived class
    company = "Info Tech"
    def showLanguage(self):
        print(f"The company name is {self.company} and he is good with {self.language} language ")

a = Employee()
b = Programmer()

b.show("Sohan")    # The name of employee is Sohan
b.printLanguage()  # out of all the language here is your language Python
b.showLanguage()   # The company name is Info Tech and he is good with Python language