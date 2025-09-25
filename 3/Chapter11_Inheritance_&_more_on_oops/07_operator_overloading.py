class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n+num.n

n = Number(1)
m = Number(5)

# print(n+m)  # TypeError: unsupported operand type(s) for +: 'Number' and 'Number'
# ye error isyliye aay kyuki humne __add__ ka use nhi kiya tha
print(n+m) # 6