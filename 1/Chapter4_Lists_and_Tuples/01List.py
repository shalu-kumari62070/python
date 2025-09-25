a = []

print(a)  #[]
print(type(a))  #<class 'list'>


friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(type(friends))  # <class 'list'>
print(friends[0])  # Apple

friends[0] = "Grapes"  # lists are mutable and list change in original value
print(friends[0])  #Grapes
print(friends)  #['Grapes', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan']

# List Slicing
print(friends[1:5])  #['Orange', 5, 345.06, False]

#add value in list
friends[6] = "hello"
print(friends)    #['Grapes', 'Orange', 5, 345.06, False, 'Aakash', 'hello']

print(len(friends))  #7

#print(friends[8])  #IndexError: list index out of range
