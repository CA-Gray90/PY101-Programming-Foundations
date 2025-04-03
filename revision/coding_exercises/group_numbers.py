# Given a list of integers, write a function group_numbers that rearranges the
# list so that all even numbers appear first, followed by all odd numbers. The
# relative order within each group (evens and odds) should be maintained.

# PSEUDOCODE:
# SET index = 0
# while index < length of list:
#   if the list[index] number is even:
#       remove it using .pop(index) and insert it using .insert(index, number)
#       increment index += 1
#   increment index += 1

def group_numbers(lst):
    index = 0
    insert_idx = 0
   
    while index < len(lst):
        current_num = lst[index]

        if current_num % 2 == 0:
            element = lst.pop(index)
            lst.insert(insert_idx, element) 
            insert_idx += 1
            index += 1

        else:
            index += 1

# def group_numbers(lst):
#     evens = []
#     odds = []

#     for num in lst:
#         if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)

#     return evens + odds

# Expected behavior:
print(group_numbers([3, 1, 2, 4, 7, 6]))
# Should output: [2, 4, 6, 3, 1, 7]