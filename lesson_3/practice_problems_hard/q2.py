# What does the last line in the following code output?

dictionary = {'first': [1]}
dict_2 = dictionary.copy()
num_list = dict_2['first']
num_list.append(2)

print(num_list)     # [1, 2]
print(dictionary)   # {first : [1, 2]}

# Line 4 we assign num_list to the value associated with the key 'first' in 
# 'dictionary', which is a the list [1]. num_list points to the same object in 
# memory as the dictionary does.

# Line 5 we append the value '2' to num_list, which mutates the list and
# dictionary stays updated

# Line 7 will output: [1, 2]
# Line 8 will output: {'first':[1, 2]}
# This is because num_list was assigned to the value of dictionary['first'], 
# which in python will bind num_list to the same object as dictionary['first'].
# They are both pointing at the same object in memory