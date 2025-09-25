l = [3, 45, 88]

# index = 0
# for i in l:
#     print(f"The item number at index {index} is {i}")
#     index +=1

# output
# The item number at index 0 is 3
# The item number at index 1 is 45
# The item number at index 2 is 88

# same program ko enumerate function se karenge
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

# output
# The item number at index 0 is 3
# The item number at index 1 is 45
# The item number at index 2 is 88