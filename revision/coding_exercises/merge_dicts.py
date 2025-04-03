# Write a function called merge_dictionaries that takes two dictionaries as
# arguments and returns a new dictionary that contains all key-value pairs from
# both dictionaries. If there are duplicate keys, the values from the second
# dictionary should override the values from the first dictionary.

def merge_dictionaries(dict_1, dict_2):
    return dict_1 | dict_2

def merge_dictionaries(dict_1, dict_2):
    result = dict(dict_1.items())
    result.update(dict_2)
    return result

# def merg

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}
print(merge_dictionaries(dict1, dict2))
# Expected output: {'a': 1, 'b': 4, 'c': 3, 'd': 5, 'e': 6}