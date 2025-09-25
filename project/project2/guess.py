from random import randint

num = randint(10,100)

a = -1
while(a != num):
    a = int(input("Guess the number = "))
    if(a < num):
        print("your guessing number is low. so please guess high number")
    elif(a >num):
        print("your guessing number is high. so please guess low number")

print(f"you guess right number {a}")