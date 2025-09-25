class Employee:
    language = "python"   # this is class attribute 
    skill = "html"

a = Employee()
a.name = "Ram"     # this is instance attribute 
print(a.name, a.language, a.skill)

b = Employee()
b.name = "Siya"
print(b.name, b.language, b.skill)

# output
# Ram python html
# Siya python html


# note:-
# Here name is instance attribute and salary and language are class attribute as they directly belong to the class.
