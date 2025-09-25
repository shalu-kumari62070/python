
with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\log.html", "r") as f:
    data = f.readlines()

lineno  = 1
for line in data:
    if("python" in line):
        print(f"yes python is present. Line no: {lineno}")
        break
    lineno +=1
else:
    print("not present")
