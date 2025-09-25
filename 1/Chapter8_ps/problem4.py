n = int(input("Enter the number = "))

def sumofNaturalnum(n):
    if(n==1):
        return 1
    return sumofNaturalnum(n-1) + n

print(sumofNaturalnum(n))

# Enter the number = 4
# 10