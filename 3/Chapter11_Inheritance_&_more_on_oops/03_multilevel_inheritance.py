class showA:
    sub  = 45-10
    print("Subtract of two number = ", sub)

class showB(showA):
    sum = (4+5)
    print("sum of two number = ", sum )

class showC(showB):
    mul =(5*2)
    print("multiply of two number = ",mul)


a = showC()

# output = 
# Subtract of two number =  35
# sum of two number =  9      
# multiply of two number =  10

