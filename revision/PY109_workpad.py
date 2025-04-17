def double_odd_indices(lst):
    return [num * 2 if idx % 2 == 1 else num for idx, num in enumerate(lst)]

# PCODE:
# List comprehension

# result = []
# LOOP through elements of list
# for each element, check if odd:
#   if odd, element * 2, append this to the list.
# else:
#   append element to list as is
# 
# return new list

print(double_odd_indices([1, 2, 3, 4, 5])  == [1, 4, 3, 8, 5])
print(double_odd_indices([10, 20, 30, 40]) == [10, 40, 30, 80])
print(double_odd_indices([]) == [])

# Write a function filter_by_age that takes a dictionary similar to the munsters
# dictionary from the curriculum and returns a new dictionary containing only
# family members who are older than a specified age.

def filter_by_age(dictionary, age_limit):
    result_dict = {}

    for name in dictionary.keys():
        age = dictionary[name]['age']
        if age >= age_limit:
            result_dict.update({name : dictionary[name]})
    
    return result_dict

# Write a function called merge_dicts that takes two dictionaries and returns
# a new dictionary. If both dictionaries have the same key, the value in the
# returned dictionary should be the sum of the values if they are numbers, or
# the concatenation if they are strings.

def merge_dicts(dict_1, dict_2):
    result = dict_1.copy()

    for key in dict_2:
        if key in result.keys():
            result[key] += dict_2[key]
        else:
            result[key] = dict_2[key]
    
    return result