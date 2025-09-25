num = int(input("Enter the number"))

table = [num*i for i in range(1, 11)]
print(table)

with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter12_ps\\table.txt", "w") as f:
    f.write(str(table))