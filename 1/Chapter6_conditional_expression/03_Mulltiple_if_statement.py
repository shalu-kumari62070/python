a = int(input("Enter your age : "))

if(a % 2 == 0):
    print("a is even")

if(a >18):
    print("you are able to give vote")
elif(a<0):
    print("You are entering invalid age")
elif(a==0):
    print("You are entering zerro which is invalid age")
else:
    print("you are not able to give vote")


# output
# Enter your age : 28
# a is even
# you are able to give vote