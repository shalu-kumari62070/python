class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The two d vector = {self.i}i + {self.j}j")
    

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The two d vector = {self.i}i + {self.j}j + {self.k}k")


a = TwoDVector(2,3)
a.show()                # The two d vector = 2i + 3j
b = ThreeDVector(4,5,6)
b.show()                # The two d vector = 4i + 5j + 6k