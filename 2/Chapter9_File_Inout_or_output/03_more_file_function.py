f = open(r"C:\Users\hp\Desktop\Python by code with harrry\Chapter9_File_I\03file.txt")

# lines = f.readlines()  # readlines always return list. it read all file 

# print(lines)
# print(type(lines))

# output
# ['python is easy\n', 'it is case sensitive\n', 'this is amazing\n', '\n']
# <class 'list'>


# readline read larta hai one line at time
# line1 = f.readline()
# print(line1, type(line1))
# python is easy
#  <class 'str'>

# line2 = f.readline()
# print(line2, type(line2))
# it is case sensitive
#  <class 'str'>

# line3 = f.readline()
# print(line3, type(line3))
# this is amazing
#  <class 'str'>

# readline ke program ko function se karenge 
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close

# output
# python is easy

# it is case sensitive

# this is amazing