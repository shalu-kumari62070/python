# using walrus operator

if(n := len([1,2,3,45,66,78,99]))>3:
    print(f"List is too long {n} elements, expected greater than 3")

# output
# List is too long 7 elements, expected greater than 3