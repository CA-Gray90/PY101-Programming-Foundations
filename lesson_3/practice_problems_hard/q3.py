# Given the following similar sets of code, what will each code snippet print?
# A)
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one # we have reassignment, so Python treats these as local variables,
    # with local scope, having no effect on global variables

one = ["one"]   # list with one element, "one"
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three) # No effect on global variables, local variables shadow global variables.

print(f"one is: {one}")     # one is: ["one"]
print(f"two is: {two}")     # two is: ["two"]
print(f"three is: {three}") # three is: ["three"]

# Function has no return value. Function has assignment within, so creates local
# variables with local scope. local variables shadow global variables. 
# global variables unmodified.

# B)
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]     # Assignment inside the function creates new local variables

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # [one]
print(f"two is: {two}")     # [two]
print(f"three is: {three}") # [three]

# Again, without the global keyword, the function creates local variables whos
# scope is only within this function. They shadow the global variables and have 
# no effect on them. The global variables remain unchanged.

# C)
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"    # This time we are referencing the first value of a list.

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # ["two"]
print(f"two is: {two}")     # ["three"]
print(f"three is: {three}") # ["one"]

# Since the list is mutable, inside the function we are mutating the first element
# of the list, which mutates the objects that the global variables reference.
# a mutating action inside a function will mutate the object that the variable
# passed in as argument references. In Python we are passing a reference to an 
# object to the function, not a copy.

# The variables 'one' 'two' 'three' inside the function are still local variables
# and shadow the variables of the same name in the global scope. 