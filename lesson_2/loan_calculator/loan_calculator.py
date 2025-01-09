import math

def display(text):
    print(f'# {text}')

def prompt():
    return input('--> ')

def yes_or_no():
    answer = prompt().casefold()
    while True:
        if answer in ['y', 'yes']:
            return True
        if answer in ['n', 'no']:
            return False
        else:
            display("Please try again, 'y' for Yes, 'n' for No")
            answer = prompt().casefold()

def welcome():
    display('Welcome to the Loan Calculator!')
    display('This Loan Calculator calculates your monthly mortgage or car'
            ' repayments')

def get_loan():
    error_message_loan = ('Invalid input. Please enter a number with numeric'
                     ' characters and/or commas only:')
    
    display('Please enter your loan amount in $ (enter numerals and commas'
            ' only):')
    loan = prompt()
    while True:
        try:
            loan = float(''.join(loan.split(',')))
        except ValueError:
            display(error_message_loan)
            loan = prompt()
        else:
            if math.isnan(loan) or math.isinf(loan):
                display(error_message_loan)
                loan = prompt()
            return loan

# loan = get_loan()
# print(f'{loan:,.2f}')
