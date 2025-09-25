class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

employee1 = Programmer("ram", 45000, 8689)
print(employee1.name, employee1.salary, employee1.pincode)

employee2 = Programmer("Siya", 78000, 9091 )  # ram 45000 8689 
print(employee2.name, employee2.salary, employee2.pincode)  # Siya 78000 9091