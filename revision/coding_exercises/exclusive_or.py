# Write a function called exclusive_or (often called xor) that takes two
# arguments and returns True when exactly one of its arguments is truthy,
# and False otherwise.

# Your implementation should use Python's logical operators (and, or, not).
# Don't use if statements or the Boolean operators == or != in your solution.

def exclusive_or(value1, value2):
    if value1 and not value2:
        return True
    elif not value1 and value2:
        return True
    else:
        return False

# Refactored:

def exclusive_or(value1, value2):
    return (value1 and not value2) or (not value1 and value2)
    
print(exclusive_or(True, False) == True)    # True
print(exclusive_or(False, True) == True)    # True
print(exclusive_or(False, False) == False)  # True
print(exclusive_or(True, True) == False)    # True