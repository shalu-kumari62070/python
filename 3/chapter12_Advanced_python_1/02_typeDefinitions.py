n: int = 5

name: str = "ram"

li : list = [4, 5]

# tu : tuple(str, int) = ("hello", 45)

# types likhane se int ,str etc ke sare method aa jate hai when we write n. ya name.

# in function 

def sum(a: int, b: int) -> int:
    return a+b

print("sum = ", sum(4,5))  # sum =  9

def greet(name: str) -> str:
    print("hello good morning, ", name)

greet("Siya")  # hello good morning,  Siya
