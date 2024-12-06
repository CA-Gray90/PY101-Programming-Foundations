def prompt(message):
    print(f'==> {message}')

def invalid_num(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
num_1 = input()

while invalid_num(num_1):   # Checks for valid input, loops back if invalid
    prompt('Invalid input entered, try again:')
    num_1 = input()

prompt("What's the second number?")
num_2 = input()

while invalid_num(num_2):
    prompt('Invalid input entered, try again:')
    num_2 = input()

prompt('''What operation would you like to perform?
1) Addition, 2) Subtraction, 3) Multiplication, 4) Division''')

operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('Invalid operation chosen, must choose 1, 2, 3 or 4')
    operation = input()

match operation:
    case '1':
        result = int(num_1) + int(num_2)
    case '2':
        result = int(num_1) - int(num_2)
    case '3':
        result = int(num_1) * int(num_2)
    case '4':
        result = int(num_1) / int(num_2)

prompt(f'The result is {result}')