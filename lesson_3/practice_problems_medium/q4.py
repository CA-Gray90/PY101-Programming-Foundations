# What will the following two lines of code output?

print(0.3 + 0.6)            # 0.9

print(0.3 + 0.6 == 0.9)     # True

# Because of the way python handles storing decimal numbers, 0.3 + 0.6 does not
# equal 0.9 exactly. Therefore 0.3 + 0.6 != 0.9

import math
print(0.3 + 0.6)            # 0.9
print(math.isclose(0.3 + 0.6, 0.9))
