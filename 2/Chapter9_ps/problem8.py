
with open(f"C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\this.txt", "r") as f:
    content = f.read()


with open(f"C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter9_ps\\this_copy.txt", "w") as f:
    f.write(content)