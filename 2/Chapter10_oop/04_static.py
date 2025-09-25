class Employee:
    language = "python"   # this is class attribute 
    salary = 12000

    @staticmethod
    def greet():
        print("good morning")

    # @staticmethod means ki humse koi v object ke property nhi chachiye means self nhi chachiye


    def greet(self):
        print("good morning", self.language)  #good morning python

a = Employee()
a.greet()  # good morning
a.greet()
