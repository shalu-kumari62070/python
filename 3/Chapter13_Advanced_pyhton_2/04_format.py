a = "{} is easy {}".format("pyhton", "language")
# or
# a = "{0} is easy {0}".format("pyhton", "language")
print(a)  # pyhton is easy language


b = "{1} is good {0}".format("Girl", "She")
print(b)  # She is good Girl

c = "{} is good {}".format("Girl", "She")
print(c)  # Girl is good She