# Tuple is immutable so we cannot change tuple

#c = (45)
#print(type(c))  #<class 'int'>
#so preventing this error we use comma
c = (45,)
print(type(c))  #<class 'tuple'>

a = (1, 2, 45, 56)

print(type(a))  #<class 'tuple'>

b = ()  # this is empty tuple
print(b)  #()
print(type(b))  #<class 'tuple'>

tl = (14, "hello", "hii", 45, 87)
print(type(tl))  #<class 'tuple'>