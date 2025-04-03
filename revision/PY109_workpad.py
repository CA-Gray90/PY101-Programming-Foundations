everest = "Everest"
kilimanjaro = "Kilimanjaro"
fuji = "Fuji"                   # Assign global variables to string objects

mountain_list = [everest, kilimanjaro, fuji]    # Assign `mountain_list` to list containing variables defined in line 1 - 3.

# print(mountain_list)
# print(repr(mountain_list[0]))

for idx in range(len(mountain_list)):
    mountain_list[idx] += " " + str(len(mountain_list[idx]))    # Mutating the list object, changing the values at each index.
                                                                # mountain_list[idx] = mountain_list[idx] + " " + str(len(mountain_list[idx]))
                                                                # mountain_list[0] = 'Everest' + " " + '7'

                                                                # We are mutating a list object using square bracket notation and indexing, changing the elements

print(mountain_list) # ['Everest 7', 'Kilimanjaro 11', 'Fuji 4']
# print(everest, kilimanjaro, fuji)
print(id(everest))
everest += "is the highest mountain"
print(id(everest))