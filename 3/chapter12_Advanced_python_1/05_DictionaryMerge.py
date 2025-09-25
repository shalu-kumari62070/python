dict1  = {1:'a', 4:'b'}
dict2 = {"ab": "hello", "gh": 78}
dict3 = {"name": "ram", "location": "lucknow"}

merged = dict1 | dict2 | dict3

print(merged)  # {1: 'a', 4: 'b', 'ab': 'hello', 'gh': 78, 'name': 'ram', 'location': 'lucknow'}

a = dict3 | dict2 | dict1
print(a)
# {'name': 'ram', 'location': 'lucknow', 'ab': 'hello', 'gh': 78, 1: 'a', 4: 'b'}

# with ke multiple file ko open kar sakte hai
with (open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\chapter12_Advanced_python_1\\file1.txt","r") as f1,
open("C:\\Users\\hp\\Desktop\\Python by code with harrry\\chapter12_Advanced_python_1\\file2.txt", "r") as f2 ):
    
    f1.read()
    f2.read()