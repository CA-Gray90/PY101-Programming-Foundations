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
   
def get_loan_duration():
    display('Please enter the loan duration in years and months.')
    display('Years:')
    duration_years = prompt()
    duration_years = valid_loan_duration(duration_years)

    display('Months:')
    duration_months = prompt()
    duration_months = valid_loan_duration(duration_months)

    return calc_loan_duration(duration_years, duration_months)
        
def valid_loan_duration(duration):
    while True:
        try:
            if duration == '':
                return 0
            duration = int(duration)
        except ValueError:
            display ('Invalid input, please enter a whole number.')
            duration = prompt()
        else:
            return duration

def calc_loan_duration(years, months):
    return (years * 12) + months

# loan = get_loan()
# print(f'{loan:,.2f}')
# duration = get_loan_duration()
# print(duration)