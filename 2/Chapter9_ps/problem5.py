words = ["donkey", "bad", "sad"]

with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\problem4.txt", "r") as f:
    data = f.read()

for word in words:
    data = data.replace(word, "######")

with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\problem4.txt", "w") as f:
    f.write(data)
