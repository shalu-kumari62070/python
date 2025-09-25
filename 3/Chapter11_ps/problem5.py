class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return self.x + other.x, self.y+other.y, self.z+other.z
    
    def __mul__(self, other):
        return self.x *other.x + self.y * other.y + self.z*other.z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
v1 = Vector(4,5,6)
v2 = Vector(2,3,4)
v3 = Vector(1,2,4)
    
print(v1 + v2)  # (6, 8, 10)
print(v1*v2)

print(v1 + v3)  # (5, 7, 10)
print(v1 * v3)  # 38    