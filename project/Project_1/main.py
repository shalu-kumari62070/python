'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
yourStr = input("Enter your choice = ")
yourDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"sanke", 0:"gun", -1:"water"}
you = yourDict[yourStr]

print(f"You choice is {reverseDict[you]} and computer choice is {reverseDict[computer]}")

if(computer == you):
    print("It's draw")
else:
    if(computer==1 and you==0):
        print("you win !")
    elif(computer==1 and you==-1):
        print("you Lose !")
    elif(computer==-1 and you==1):
        print("you win !")
    elif(computer==0 and you==1):
        print("you lose !")
    elif(computer==0 and you==-1):
        print("you lose !")
    elif(computer==-1 and you==0):
        print("you win !")
    else:
        print("Something went Wrong")
    