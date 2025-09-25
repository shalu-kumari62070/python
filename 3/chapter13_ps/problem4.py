def divisible(n):
    if(n%5 == 0):
        return True
    else:
        return False

li = [12, 33, 40, 88, 30, 60]

s = filter(divisible, li)
print(s)  # <filter object at 0x000001F72B226B00>
print(list(s))   # [40, 30, 60]