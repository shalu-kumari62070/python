word = "donkey"

with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\problem4.txt", "r") as f:
    data = f.read()

newdata = data.replace(word, "######")

with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\problem4.txt", "w") as f:
    f.write(newdata)
        