try:
    a = int(input("Enter first number = "))
    b = int(input("Enter second number = "))
    print("answer = ", (a/b))
except ZeroDivisionError as z:
    print("infinty")

# output
# Enter first number = 6
# Enter second number = 0
# infinty