print('Welcome to Calculator!')

# Ask the user for the first number
print("What's the first number?")
num_1 = input()

# Ask the user for the second number
print("What's the second number?")
num_2 = input()

# Ask the user for an operation to perform
print(
    ('What operation would you like to perform?\n'
     '1 - Addition, 2 - Subtraction, 3 - Multiplication, 4 - Division')
)
operation = input()

# perform the calculation
if operation == '1':
    result = int(num_1) + int(num_2)
elif operation == '2':
    result = int(num_1) - int(num_2)
elif operation == '3':
    result = int(num_1) * int(num_2)
elif operation == '4':
    result = int(num_1) / int(num_2)

# Print out the result
print(f'The result is {result}')