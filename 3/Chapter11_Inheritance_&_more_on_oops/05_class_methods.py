class Employee:
    a = 45


    # @classmethod se class attribute ki value aati hai
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 78
e.show()  # The class attribute of a is 45

# if we don't use @classmethod the output  = The class attribute of a is 78

# note :- self means wo object jis pe method chal raha hai