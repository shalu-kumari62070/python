word = "python"

with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\log.html", "r") as f:
    data = f.read()
    
if( word in data ):
    print("yes present")
else:
    print("not present")