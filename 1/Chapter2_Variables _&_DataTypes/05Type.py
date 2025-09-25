# type() function is used to find data type of a given variable

a = "Ram"
print(type(a))  #<class 'str'>

e = "45"
print(type(e))  #<class 'str'>

b = 45
print(type(b)) #<class 'int'>

c = 5.6
print(type(c)) #<class 'float'>

d = True
print(type(d)) #<class 'bool'>


#typeCasting

f = "45.23"
g = float(f)
print(type(g))  #<class 'float'>

h = 45
i = str(h)
print(type(i)) #<class 'str'>

ab = 52.6
bc = int(ab)
print(type(bc))  #<class 'int'>

#note we can not convert string into integer 
