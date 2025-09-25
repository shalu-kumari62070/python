n1 = int(input("Enter number 1 = "))
n2 = int(input("Enter number 2 = "))
n3 = int(input("Enter number 3 = "))
n4 = int(input("Enter number 4 = "))

if(n1>n2 and n1>n3 and n1>n4 ):
    print(f"n1 is greater {n1}")
elif(n2>n1 and n2>n3 and n2>n4):
    print(f"n2 is greater {n2}")
elif(n3>n1 and n3>n2 and n3>n4):
    print(f"n3 is greater {n3}")
else:
    print(f"n4 is greater {n4}")


#output
# Enter number 1 = 25
# Enter number 2 = 2
# Enter number 3 = 78
# Enter number 4 = 22
# n3 is greater 78