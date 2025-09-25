li = ["pyhton", "Java", "an", "Rohan", "johan"]

def rem(li, word):
    l = []
    for item in li:
        if (item != word):  # ya  if not(item == word): 
            l.append(item.strip(word))
    return l

print(rem(li, "an"))  #['pyhto', 'Jav', 'Roh', 'joh']