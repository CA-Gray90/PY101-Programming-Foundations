# What will the following code output?

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

# This will mutate the dictionary, since dicts are mutable objects.
print(munsters)

# In python, dictionaries are mutable, and when passed to a function, a
# a reference is passed, not a copy. Therefore, with this code, the original
# dictionary is modified