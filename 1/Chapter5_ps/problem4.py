s = set()

s.add(20)
s.add(20.0)
s.add('20')

print(s)  # {20, '20'}
print(len(s)) # 2

#better understanding

a = 1 == 1.0
print(a)  #True

b = 1 == 1.8
print(b)  #False
print(type(b))  #<class 'bool'>