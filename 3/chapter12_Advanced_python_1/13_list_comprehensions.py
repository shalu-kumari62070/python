myList = [2, 4, 3, 5]

# squaredList =[]
# for i in myList:
#     squaredList.append(i*i)
# print(squaredList)           # [4, 16, 9, 25]

# same program ko hum list comprehension se karenge

squaredList = [i*i for i in myList]
print(squaredList)   # [4, 16, 9, 25]


