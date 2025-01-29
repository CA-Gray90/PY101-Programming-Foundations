# What do you expect to happen when the greeting variable is referenced in the
# last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

# line 5 is never accessed since `if False` evaluates to False and skips
# the if code block. Therefore `greeting` is never defined (in Python).
# We get a NameError