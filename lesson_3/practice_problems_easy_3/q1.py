# Write two different ways to remove all of the elements from the following
# list:

numbers = [1, 2, 3, 4]
number2 = numbers

# numbers.clear()   # clears original list
# numbers = []      # does not clear the original list, reassigns numbers to an new empty list object

while numbers:      # clears original list
    numbers.pop()

print(numbers)
print(number2)