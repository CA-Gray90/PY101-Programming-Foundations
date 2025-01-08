# IMPORTS
import json
import math
import os
import time

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# FUNCTIONS
def prompt(message, index=None):
    if index is not None:
        print(f'==> {MESSAGES[LANG][message][index]}')
    else:
        print(f'==> {MESSAGES[LANG][message]}')

def language_select():
    print("! Please select a language: "
           "'en' for English, 'au' for Australian")
    answer = input().casefold()

    while True:
        if answer in ['en', 'english']:
            print('English selected...')
            time.sleep(1)
            return 'en'
        if answer in ['au', 'australian']:
            print('Aussie lingo selected...')
            time.sleep(1)
            return 'au'
        print("Invalid input, please enter either 'en' or 'au' ")
        answer = input().casefold()

def invalid_num(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    else:
        if math.isnan(float(number_str)):
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

def get_number():
    user_num = input()

    while invalid_num(user_num):   # Validity Check
        prompt('invalid_num_message')
        user_num = input()

    return float(user_num)

def get_operator():
    user_op = input()
    while user_op not in OPERATION_DICT: # Operation validity check
        prompt('invalid_operation_message')
        user_op = input()
    return user_op

def calculation(operation_choice, num_1, num_2):
    if num_2 == 0 and operation_choice == '4':    # Check for division by Zero
        prompt('division_by_zero')
        return None
    
    return OPERATION_DICT[operation_choice][1](num_1, num_2)

# CONSTANTS
OPERATION_DICT = {
    '1' : ['+', (lambda x, y: x + y)], 
    '2' : ['-', (lambda x, y: x - y)],
    '3' : ['*', (lambda x, y: x * y)],
    '4' : ['/', (lambda x, y: x / y)]
}

# PROGRAM START
os.system('clear')
LANG = language_select()

os.system('clear')
prompt('greeting')

while True:
    prompt('num_prompt', 0)
    num_1 = get_number()

    prompt('num_prompt', 1)
    num_2 = get_number()

    prompt('operation_message')
    prompt('operation_options')
    operation = get_operator()

    RESULT = calculation(operation, num_1, num_2)

    if RESULT is not None: # Check that we didn't attempt division by zero
        prompt('result_message')
        print(f'{num_1} {OPERATION_DICT[operation][0]} {num_2} = {RESULT}')

    prompt('try_again_message') # Try again
    user_answer = input()
    if try_again(user_answer):
        prompt('try_again_answer', 0)
        time.sleep(1)
        os.system('clear')
    else:
        prompt('try_again_answer', 1)
        break