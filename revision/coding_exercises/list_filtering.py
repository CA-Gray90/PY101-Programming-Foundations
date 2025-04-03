# Write a function that takes a list of integers and returns a new list
# containing only the even numbers from the original list. Implement this
# function twice: once using a for loop and once using a while loop.

# for loop:

def filter_list(lst):
    result = []
    
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    
    return result

def filter_list(lst):
    return [num for num in lst if num % 2 == 0]

print(f'for loop: {filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}')

# while loop:

def filter_list(lst):
    result = []
    index = 0

    while index < len(lst):
        num = lst[index]

        if num % 2 == 0:
            result.append(num)
        index += 1

    return result

print(f'while loop: {filter_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}')

# Output: [2, 4, 6, 8, 10]