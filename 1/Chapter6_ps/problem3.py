p1 = "Make a lot of Money"
p2 = "buy now"
p3 = "Click this"

message = input("Enter your comment ")

if(message in p1 or message in p2 or message in p3):
    print("this commnet is spam")
else:
    print("this comment is not spam")