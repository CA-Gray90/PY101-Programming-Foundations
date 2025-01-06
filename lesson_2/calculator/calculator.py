# FUNCTIONS
def prompt(message):
    print(f'==> {message}')

def invalid_num(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def try_again(answer):
    answer = answer.casefold()
    while True:
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        prompt("Invalid response, please enter either 'y' or 'n':")
        answer = input()

# PROGRAM START
prompt('Welcome to Calculator!')

while True:
    prompt("What's the first number?")
    num_1 = input()

    while invalid_num(num_1):   # Validity Check
        prompt('Invalid input entered, must be a whole number. Try again:')
        num_1 = input()

    prompt("What's the second number?")
    num_2 = input()

    while invalid_num(num_2):
        prompt('Invalid input entered, try again:')
        num_2 = input()

    prompt('''What operation would you like to perform?
    (1) Addition, (2) Subtraction, (3) Multiplication, (4) Division''')
    operation = input()

    while operation not in ['1', '2', '3', '4']:    # Operation validity check
        prompt('Invalid operation chosen,'
               ' must choose 1, 2, 3 or 4. Try again:')
        operation = input()

    match operation:
        case '1':
            result = int(num_1) + int(num_2)
        case '2':
            result = int(num_1) - int(num_2)
        case '3':
            result = int(num_1) * int(num_2)
        case '4':
            if num_2 != '0':    # Check for division by Zero
                result = int(num_1) / int(num_2)
            else:
                print('Cannot Divide by Zero!')
                result = None

    if result is not None:
        prompt(f'The result is {result}')

    prompt('Would you like to try again? y/n')
    user_answer = input()
    if try_again(user_answer):
        prompt('Starting again...')
    else:
        prompt('Exiting Program...')
        break