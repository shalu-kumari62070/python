# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")

# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")

# class Manager(Programmer):
#     def __init__(self):
#         print("Constructor of Manager")


# a = Employee()    # Constructor of Employee
# b = Programmer()  # Constructor of Programmer
# c = Manager()     # Constructor of Manager


# here we use super key word by using this we print parent class constructor

class Employee:
    def __init__(self):
        print("Constructor of Employee")

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")

a = Manager()
# output
# Constructor of Programmer
# Constructor of Manager
