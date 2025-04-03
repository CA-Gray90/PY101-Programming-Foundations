# Write a function called filter_strings that takes a list of strings and
# returns a new list containing only the strings that have more than 5
# characters. Use a list method in your implementation.

def filter_strings(lst):
    result = []

    for element in lst:
        if len(element) > 5:
            result.append(element)
    
    return result

def filter_strings(lst):
    return [element for element in lst if len(element) > 5]

# Expected behavior:
print(filter_strings(['apple', 'banana', 'kiwi', 'watermelon', 'fig']))
# Should output: ['banana', 'watermelon']