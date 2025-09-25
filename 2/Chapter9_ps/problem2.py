import random

def game():
    print("You are playing game")
    score  = random.randint(1,50)
    print("your score is ", score)
    with open(r"C:\Users\hp\Desktop\Python by code with harrry\Chapter9_ps\hiscore.txt","r") as f:
        highScore = f.read()
        if( highScore==""):
            highScore = 0
        else:
            highScore = int(highScore)
    print("Your high score is ", highScore)
    with open(r"C:\Users\hp\Desktop\Python by code with harrry\Chapter9_ps\hiscore.txt","w") as f:
        if(score>highScore):
            f.write(str(score))
    # return score 

game()