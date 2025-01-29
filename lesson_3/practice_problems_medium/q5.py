nan_value = float('nan')

print(nan_value == float('nan')) # False

# Can't remember exactly why, but nan - Not A Number, does not equal itself. It
# represents a non meaningful number and therefore cannot be equal to another
# nan.

import math

print(math.isnan(nan_value))    # True

# Using the math module .isnan() method to check if nan_value is nan