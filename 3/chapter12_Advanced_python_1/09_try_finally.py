try:
    a = int(input("enter the number = "))
    print(a)

except Exception as b:
    print(b)

finally:
    print("I am inside the finally")
#note finally always run hota hai

# enter the number = 99
# 99
# I am inside the finally

# enter the number = hii
# invalid literal for int() with base 10: 'hii'
# I am inside the finally