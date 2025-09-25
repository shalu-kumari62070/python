#Dictionary is key value pair

#Properties of Dictionary
# it is unordered
# it is mutable
# it is indexed
# cannot conatin duplicate keys
# duplicate values are allow but duplicate keys are not allow

marks = {
    "harry" :100,
    "subham":200,
    "rohab" : 300,
    "li" : [2,45,68, 10],
    "hii" : "hello",
    "how" : (24, 25, 10),
    1 : 10,
    22 : "fine"
}

print(len(marks))  #8

print(type(marks))  #<class 'dict'>

print(marks["harry"])  #100

print(marks["li"])  #[2, 45, 68, 10]

print(marks[1])  #10

print(marks["how"])  #(24, 25, 10)


b = {}
print(type(b))  #<class 'dict'>

a = tuple({})
print(type(a))  #<class 'tuple'>

c = dict()
print(type(c))  #<class 'dict'>

d = ()
print(type(d))  #<class 'tuple'>

