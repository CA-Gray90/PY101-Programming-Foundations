# Given a number and a list, determine whether the number is included in the list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# or

# for number in numbers:
    # if number == number1:
    #     print(True)
    # print(False)

print(any(number == number1 for number in numbers))
print(any(number == number2 for number in numbers))

# This solution uses a list comprehension passed into the any function to check
# for any `True` elements within that list. That indicates that number1 or
# number2 does indeed exist in numbers