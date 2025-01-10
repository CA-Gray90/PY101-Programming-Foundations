import math

def display(text):
    print(f'# {text}')

def prompt(prefix=''):
    return input(f'--> {prefix}')

def ask_yes_or_no():
    answer = prompt().casefold()
    while True:
        if answer in ['y', 'yes']:
            return True
        if answer in ['n', 'no']:
            return False
        else:
            display("Please try again, 'y' for Yes, 'n' for No")
            answer = prompt()

def welcome():
    display('Welcome to the Loan Calculator!')
    display('This Loan Calculator calculates your monthly mortgage or car'
            ' repayments.\n*Interest is assumed to be compounded monthly.')

def get_loan():
    display('Please enter your loan amount in $ (enter numerals and commas'
            ' only):')
    loan = prompt('$')

    error_message_loan = ('Invalid input. Please enter a $ amount with numeric'
                     ' characters and/or commas only:')
    while True:
        try:
            loan = float(''.join(loan.split(',')))
        except ValueError:
            display(error_message_loan)
            loan = prompt('$')
        else:
            if math.isnan(loan) or math.isinf(loan):
                display(error_message_loan)
                loan = prompt('$')
            return loan
   
def get_loan_duration():
    display('Please enter the loan duration in Years and Months.')
    duration_years = prompt('Years:')
    duration_years = valid_loan_duration(duration_years)

    duration_months = prompt('Months:')
    duration_months = valid_loan_duration(duration_months)

    return loan_total_months(duration_years, duration_months)
        
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

def loan_total_months(years, months):
    return (years * 12) + months

def get_apr():
    display('What is your Annual Percentage Rate, or APR?'
            ' (Please enter as a %):')
    user_apr = prompt('%')

    error_message_apr = 'Invalid input, please enter a percentage out of 100:'
    while True:
        if user_apr == '':
            return 0

        try:
            user_apr = float(user_apr)
        except ValueError:
            display(error_message_apr)
            user_apr = prompt('%')
            continue
        else:
            if math.isnan(user_apr) or math.isinf(user_apr):
                display(error_message_apr)
                user_apr = prompt('%')
                continue

        if user_apr >= 0 and user_apr <= 100:
            return (user_apr / 100)
        display(error_message_apr)

def monthly_interest_rate(apr):
    return (apr / 12)

def monthly_payment(loan, monthly_interest, duration_months):
    monthly_payment = loan * \
        (monthly_interest / (1 - (1 + monthly_interest)**(-duration_months)))
    
    return monthly_payment

def try_again():
    display('Would you like to calculate another loan repayment? y/n')
    if ask_yes_or_no():
        return True
    return False

# Program Start #

# welcome()
# while True:
#     USER_LOAN = get_loan()
#     USER_DURATION = get_loan_duration()
#     YEARLY_APR = get_apr()
#     MONTHLY_APR = monthly_interest_rate(YEARLY_APR)
#     MONTHLY_REPAYMENT = monthly_payment(USER_LOAN, MONTHLY_APR, USER_DURATION)
#     print(f'{MONTHLY_REPAYMENT:.2f}')
#     if not try_again():
#         break