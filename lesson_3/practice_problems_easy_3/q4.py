# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy() # shallow copy
my_list2[0]['first'] = 42 # change value of key-value pair in dict at index 0
print(my_list1) # shallow copies still reference the same nested objects

# This will output:
# [{"first": "42"}, {"second": "value2"}, 3, 4, 5]

# .copy() performs a shallow copy, that is, a new list is created, however, the
# nested elements within that list still point to the same objects as the 
# original list.

# A shallow copy only makes a duplicate of the outermost layer, any nested layers
# reference the same objects as the original reference(variable, identifier)



