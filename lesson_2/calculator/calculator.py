# IMPORTS
import json

with open('calculator_messages.json', 'r') as file:
    messages = json.load(file)

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
        prompt(messages['invalid_try_again'])
        answer = input()

# PROGRAM START
prompt(messages['greeting'])

while True:
    prompt(messages['num_prompt'][0])
    num_1 = input()

    while invalid_num(num_1):   # Validity Check
        prompt(messages['invalid_num_message'])
        num_1 = input()

    prompt(messages['num_prompt'][1])
    num_2 = input()

    while invalid_num(num_2):
        prompt(messages['invalid_num_message'])
        num_2 = input()

    prompt(messages['operation_message'])
    prompt(messages['operation_options'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:    # Operation validity check
        prompt(messages['invalid_operation_message'])
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
                print(messages['division_by_zero'])
                result = None

    if result is not None:
        prompt(f'{messages['result_message']} {result}')

    prompt(messages['try_again_message'])
    user_answer = input()
    if try_again(user_answer):
        prompt(messages['try_again_answer'][0])
    else:
        prompt(messages['try_again_answer'][1])
        break