s = {1, 45, 33, "Python", "react"}
print(s, type(s))    #{'Python', 1, 33, 'react', 45} <class 'set'>

s.add(566)
print(s)        #{'Python', 1, 33, 'react', 566, 45}
print(type(s))  # <class 'set'>

#print(s.clear())  #None
# s.clear()  # this empty the set
# print(s)  #set()

print(len(s))  #6

s.remove(45)
print(s, type(s))  #{1, 33, 'Python', 566, 'react'} <class 'set'>

# s.pop()
# print(s)  #{33, 566, 'Python', 'react'}
