def foo(param="no"): # returns 'yes' whether a object passed to it or not
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no") # 

# What will the following invocation return?

print(bar(foo()))

# False
# We pass in foo() with no arguments to bar(). foo() is evaluated first and 
# returns 'yes', which is passed to bar and
# checked for equality against 'no', which evaluates to False. In this case, 
# it doesnt matter what the or operation returns since Python will short circuit
# the and operation and return False.