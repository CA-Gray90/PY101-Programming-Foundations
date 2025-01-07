# IMPORTS
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# FUNCTIONS
def prompt(message, index=None):
    if index is not None:
        print(f'==> {MESSAGES[LANG][message][index]}')
    else:
        print(f'==> {MESSAGES[LANG][message]}')

def invalid_num(number_str):
    try:
        float(number_str)
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
        prompt('invalid_try_again')
        answer = input()

def language_select():
    print("! Please select a language: "
           "'en' for English, 'au' for Australian")
    answer = input().casefold()

    while True:
        if answer in ['en', 'english']:
            return 'en'
        if answer in ['au', 'australian']:
            return 'au'
        print("Invalid input, please enter either 'en' or 'au' ")
        answer = input().casefold()

LANG = language_select()

operation_dict = {
    '1' : '+',
    '2' : '-',
    '3' : '*',
    '4' : '/'
}

# PROGRAM START
prompt('greeting')

while True:
    prompt('num_prompt', 0)
    num_1 = input()

    while invalid_num(num_1):   # Validity Check
        prompt('invalid_num_message')
        num_1 = input()

    num_1 = float(num_1)

    prompt('num_prompt', 1)
    num_2 = input()

    while invalid_num(num_2):
        prompt('invalid_num_message')
        num_2 = input()

    num_2 = float(num_2)

    prompt('operation_message')
    prompt('operation_options')
    operation = input()

    while operation not in ['1', '2', '3', '4']:    # Operation validity check
        prompt('invalid_operation_message')
        operation = input()

    match operation:
        case '1':
            RESULT = num_1 + num_2
        case '2':
            RESULT = num_1 - num_2
        case '3':
            RESULT = num_1 * num_2
        case '4':
            if num_2 != '0':    # Check for division by Zero
                RESULT = num_1 / num_2
            else:
                prompt('division_by_zero')
                RESULT = None

    if RESULT is not None:
        prompt('result_message')
        print(f'{num_1} {operation_dict[operation]} {num_2} = {RESULT}')

    prompt('try_again_message')
    user_answer = input()
    if try_again(user_answer):
        prompt('try_again_answer', 0)
    else:
        prompt('try_again_answer', 1)
        break