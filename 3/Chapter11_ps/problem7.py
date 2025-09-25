class Vector:
    def __init__(self, l):
        self.l = l
     
    
    def __len__(self):
        return len(self.l)
    
v1 = Vector([4,5,6,78,23])

print(len(v1))  # 5