# for file1
try:
    with open(r"file1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

# for file2
try:
    with open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\Chapter12_ps\\file2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

# for file3
try:
    with open(r"file3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


# output = 
# [Errno 2] No such file or directory: 'file1.txt'
# hello this is file two
# [Errno 2] No such file or directory: 'file3.txt'
