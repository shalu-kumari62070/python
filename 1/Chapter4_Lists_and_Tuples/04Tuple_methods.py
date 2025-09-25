a = (14, 66, "hello", 66, "hii", 45, 87, 66, 5)

print(len(a))  #9

print(a.count(66))  # 3

print(a.index("hello"))  #2

#repeated  tuple
b = (45, 1, 5, 2)
print(b*3)  # (45, 1, 5, 2, 45, 1, 5, 2, 45, 1, 5, 2)

#concatition tuple
print(a+b)  # (14, 66, 'hello', 66, 'hii', 45, 87, 66, 5, 45, 1, 5, 2)

print(a, b)  #(14, 66, 'hello', 66, 'hii', 45, 87, 66, 5) (45, 1, 5, 2)

#membership operator
print(2 in b)  # True
print(3 in b)  # False

#min and max
print(min(b))  # 1
print(max(b))  # 45

#Slicing
# In case of slicing we receive new tuple
print(a[2:6])  #('hello', 66, 'hii', 45)

#Unpacking tuple
g = (45, 78, 29)
i, j, k = g
print(i, j, k)  # 45 78 29
print(g)        #(45, 78, 29)


 