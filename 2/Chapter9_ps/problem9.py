
with open(f"C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\file1.txt", "r") as f:
    content1 = f.read()

with open(f"C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\file2.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes match")
else:
    print("not match")