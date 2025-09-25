from functools import reduce

l = [78,45689, 258, 11001, 789]

def greatest(a, b):
    if(a>b):
        return a
    else:
        return b

print(reduce(greatest, l))   # 45689

    