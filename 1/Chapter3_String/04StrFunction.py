name = "Hello world"

print(len(name)) #11

print(name.endswith("ld")) #True

print(name.endswith("od")) #False
 
print(name.startswith("H"))  #True

print(name.startswith("h"))  #False

a = "how are you"
print(a.capitalize())  #How are you 
#capitalize() ye index 0 ko ki capital me karta hai

print(a.upper())  #HOW ARE YOU

print(a.lower())  #how are you

b =  "Pyhton is very very easy language"

print(b.replace("very", "easy"))  #Pyhton is easy easy easy language