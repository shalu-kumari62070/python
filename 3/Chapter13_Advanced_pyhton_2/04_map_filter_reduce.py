# Map example
li = [4, 56, 2, 3]

square = lambda n:n*n

sqlist = map(square, li)
print(sqlist)        # <map object at 0x0000017A26346980>
print(list(sqlist))  # [16, 3136, 4, 9]

# Filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, li)
print(onlyEven)        # <filter object at 0x00000291527D6D70>
print(list(onlyEven))  # [4, 56, 2]


ev = map(even, li)
print("here we try to use map ", list(ev))
# here we try to use map  [True, True, True, False]
# if we return "yes" in the palce of True so we get yes in the output

# Reduce example
from functools import reduce
def sum(a, b):
    return a + b

l = [1,4,3]
add = reduce(sum, l)
print(add)   # 8

a = [2,4,3,5]
mul = lambda x,y:x*y
ans =  reduce(mul, a)
print(ans)  # 120

