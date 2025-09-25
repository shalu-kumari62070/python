# f = open(r"C:\Users\hp\Desktop\Python by code with harrry\Chapter9_File_I\file.txt")
# data = f.read()
# print(data)   # Pyhton is very easy language 
# f.close()

# the same work can be done by using with statement
# in with statement f.close() is not require because with statement automatically close the file

with open(r"C:\Users\hp\Desktop\Python by code with harrry\Chapter9_File_I\file.txt") as f:
    print(f.read())  # Pyhton is very easy language 