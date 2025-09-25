d = {}

name1 = input("Enter your name = ")
lang1 = input("Enter your favourite language = ")
d.update({name1 : lang1})

name2 = input("Enter your name = ")
lang2 = input("Enter your favourite language = ")
d.update({name2 : lang2})

name3 = input("Enter your name = ")
lang3 = input("Enter your favourite language = ")
d.update({name3 : lang3})

name4 = input("Enter your name = ")
lang4 = input("Enter your favourite language = ")
d.update({name4 : lang4})

print(d)

#output 
# Enter your name = Siya
# Enter your favourite language = Hindi
# Enter your name = Ram
# Enter your favourite language = Sanskarti
# Enter your name = Ritu
# Enter your favourite language = English
# Enter your name = Deepa
# Enter your favourite language = Bangali
# {'Siya': 'Hindi', 'Ram': 'Sanskarti', 'Ritu': 'English', 'Deepa': 'Bangali'}