marks = {
    "harry" :100,
    "li" : [2,45,68, 10],
    "hii" : "hello",
    "how" : (24, 25, 10),
    1 : 10,
    22 : "fine"
}

print(marks.get(1))  #10
print(marks.get("harry2"))  # None
print(marks("harry2"))      # TypeError: 'dict' object is not callable

print(marks.items())  #dict_items([('harry', 100), ('li', [2, 45, 68, 10]), ('hii', 'hello'), ('how', (24, 25, 10)), (1, 10), (22, 'fine')])
print(marks.keys())   #dict_keys(['harry', 'li', 'hii', 'how', 1, 22])
print(marks.values()) #dict_values([100, [2, 45, 68, 10], 'hello', (24, 25, 10), 10, 'fine'])

#upadate() :- ye add karta or value me change v karta hai
marks.update({"harry" : 99})
print(marks)  #{'harry': 99, 'li': [2, 45, 68, 10], 'hii': 'hello', 'how': (24, 25, 10), 1: 10, 22: 'fine'}

print(marks.update({"renu":45})) #None

marks.update({"renu":45})
print(marks)  #{'harry': 99, 'li': [2, 45, 68, 10], 'hii': 'hello', 'how': (24, 25, 10), 1: 10, 22: 'fine', 'renu': 45}

#or
#marks.update({"harry" : 99, "renu":45})  #output will be same

marks.pop("how")
print(marks)  #{'harry': 99, 'li': [2, 45, 68, 10], 'hii': 'hello', 1: 10, 22: 'fine', 'renu': 45}




