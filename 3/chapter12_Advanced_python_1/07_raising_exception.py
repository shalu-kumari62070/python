a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("we can not divide by zero")
    # raise se program crash ho jata hai taki programmer apni galti ko thik kare
else:
    print(f"The division a/b is {a/b}")

# Enter a number: 4
# Enter second number: 2
# The division a/b is 2.0

# Enter a number: 5
# Enter second number: 0
# Traceback (most recent call last):
#   File "c:\Users\hp\Desktop\Python by code with harrry\chapter12_Advanced_python_1\07_raising_exception.py", line 5, in <module>
#     raise ZeroDivisionError("we can not divide by zero")
# ZeroDivisionError: we can not divide by zero


# isi program ko except se karenge

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

try:
    print(f"divison = {a/b}")

except ZeroDivisionError as z:
    print(z)

# Enter a number: 4
# Enter second number: 2
# divison = 2.0

# Enter a number: 8
# Enter second number: 0
# division by zero