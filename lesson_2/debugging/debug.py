# learning pdb

import pdb

# counter = 1

# while counter <= 5:
#     print(counter)
#     pdb.set_trace()  # Add breakpoint
#     counter += 1

cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocoa'):
    cats += [name]
    # pdb.set_trace()

print(cats)