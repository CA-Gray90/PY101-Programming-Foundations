# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())  # This will print the dict, {prop1 : "hi there"}
print(second()) # the return statement returns None by default if there is no
# expression after the return keyword on the same line. In Python, any indented
# code that comes beneath the return keyword is never accessed.