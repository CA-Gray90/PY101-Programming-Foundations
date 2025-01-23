# How would you verify whether the data structures assigned to the variables
# numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)
print(type(table) is list)

# LS Solution:
isinstance(numbers, list)  # True
isinstance(table, list)    # False

# isinstance() is used to check whether an object is of a particular class or 
# data type. Can be used with built in types (int, float, str, etc)

