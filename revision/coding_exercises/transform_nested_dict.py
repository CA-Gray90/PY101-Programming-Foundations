# Write a function called transform_nested_dict that takes a nested dictionary
# as input. The function should return a new dictionary where:

# -  All string values are converted to uppercase
# -  All integer values are doubled
# -  All list values have their elements sorted
# -  All nested dictionaries are also transformed according to these rules

def transform_nested_dict(dictionary):
    from copy import deepcopy

    result_dict = deepcopy(dictionary)

    for key, value in result_dict.items():
        if type(value) is str:
            result_dict[key] = value.upper()
        elif type(value) is int:
            result_dict[key] = value * 2
        elif type(value) is list:
            result_dict[key].sort()
        elif type(value) is dict:
            for k, v in value.items():
                if type(v) is str:
                    value[k] = v.upper()
                elif type(v) is int:
                    value[k] = v * 2
                elif type(v) is list:
                    value[k].sort()
    
    return result_dict

# Refactored Version:

def transform_nested_dict(d):
    '''
    Returns a deep copy of the original dictionary passed in as argument with
    values sorted according to:
    
    -  All string values are converted to uppercase
    -  All integer values are doubled
    -  All list values have their elements sorted
    -  All nested dictionaries are also transformed according to these rules
    '''

    from copy import deepcopy

    result_dict = deepcopy(d)

    def sort_values(dic):
        '''
        Sorts all values in dic including those in nested dicts according to
        the following rules:
        
        -  All string values are converted to uppercase
        -  All integer values are doubled
        -  All list values have their elements sorted
        -  All nested dictionaries are also transformed according to these
        rules
        '''

        for key, value in dic.items():
            if isinstance(value, str):
                dic[key] = value.upper()
            elif isinstance(value, int):
                dic[key] = value * 2
            elif isinstance(value, list):
                dic[key].sort()
            elif isinstance(value, dict):
                sort_values(value)

    sort_values(result_dict)

    return result_dict

# Example input:
data = {
    'name': 'python',
    'version': 3,
    'features': ['easy', 'powerful', 'readable'],
    'details': {
        'creator': 'guido',
        'year': 1991,
        'influences': ['abc', 'lisp', 'c']
    }
}

result = transform_nested_dict(data)

print(result)

# Expected output:
# {
#     'name': 'PYTHON',
#     'version': 6,
#     'features': ['easy', 'powerful', 'readable'],  # Sorted alphabetically
#     'details': {
#         'creator': 'GUIDO',
#         'year': 3982,
#         'influences': ['abc', 'c', 'lisp']  # Sorted alphabetically
#     }
# }
