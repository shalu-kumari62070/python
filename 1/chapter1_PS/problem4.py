import os

directory_path = '/codesoft'

contents = os.listdir(directory_path)

for item in contents:
    print(item)