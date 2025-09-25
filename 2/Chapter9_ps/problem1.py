f = open(r"C:\Users\hp\Desktop\Python by code with harrry\Chapter9_ps\poem.txt","r")
content = f.read()
if "Twinkle" in content:
    print("The word Twinkle is present")
else:
    print("The word Twinkle is not present")

f.close()

# output
# The word Twinkle is present
