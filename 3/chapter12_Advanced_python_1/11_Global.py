a = 77

def fun():
    a = 8
    print(a)

# fun()     # 8
# print(a)  # 77


b = 55
def hii():
    global b
    b = 42
    print(b)

hii()     # 42
print(b)  # 42
