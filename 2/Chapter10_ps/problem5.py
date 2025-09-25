from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


a = Train(455)
a.book("Rampur","Delhi")        # Ticket is booked in train no : 455 from Rampur to Delhi
a.getStatus()                   # Train no: 455 is running on time
a.getFare("Rampur", "Delhi")    # Ticket is booked in train no : 455 from Rampur to Delhi is 5340
