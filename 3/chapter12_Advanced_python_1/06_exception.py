try:
    a = int(input("enter the number = "))
    print(a)

except Exception as b:
    print(b)

#ouptut
# enter the number = 5
# 5

# output 
# enter the number = hii  
# invalid literal for int() with base 10: 'hii'


# Example of error
# except ValueError as v:
#     print(v)

# except TypeError
