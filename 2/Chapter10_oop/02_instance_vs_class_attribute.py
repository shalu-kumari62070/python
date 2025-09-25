class Employee:
    language = "python"   # this is class attribute 
    skill = "html"

a = Employee()
a.language = "JavaScript"
print(a.language, a.skill)   # JavaScript html

# Note :- jab instance attribute nhi milta hai to class attribute print hota 
# Note :- jab instance attribute mil jata hai to class attribute print nhi hota hai