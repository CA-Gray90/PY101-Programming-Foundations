import math
import os

def display(text):
    print(f'# {text}')

def prompt(prefix=''):
    return input(f'--> {prefix}')

def yes_or_no(answer):
    answer = answer.casefold()
    while True:
        if answer in ['y', 'yes']:
            return True
        if answer in ['n', 'no']:
            return False
        display("Please try again; 'y' for Yes, 'n' for No")
        answer = prompt()

def welcome():
    display('Welcome to the Loan Calculator!')
    print()
    display('This Loan Calculator calculates your monthly mortgage or car'
            ' repayments.\n*Interest is assumed to be compounded monthly.')
    print()

def enter_to_continue():
    while True:
        display("Press 'enter' to continue.")
        input()
        break

def get_loan():
    display('Please enter your loan amount in $ (enter numerals and commas'
            ' only):')
    loan = prompt('$')

    error_message_loan = ('Invalid input. Please enter a positive dollar'
                          ' amount. Numbers and commas only:')
    while True:
        try:
            loan = float(''.join(loan.split(',')))

            if math.isnan(loan) or math.isinf(loan) or loan < 0:
                raise ValueError
        except ValueError:
            display(error_message_loan)
            loan = prompt('$')
            continue
        return loan

def get_loan_duration():
    while True:
        display('Please enter the loan duration in Years and Months.')
        duration_years = prompt('Years: ')
        duration_years = valid_loan_duration(duration_years)

        duration_months = prompt('Months: ')
        duration_months = valid_loan_duration(duration_months)

        if (duration_months + duration_years) == 0:
            display('Duration must be at least 1 month.')
            continue
        if duration_months >= 12:
            duration_years = duration_years + duration_months // 12
            duration_months = duration_months % 12
        return (duration_years, duration_months)

def valid_loan_duration(duration):
    while True:
        if duration == '':                        # If field is left blank
            return 0
        try:
            duration = int(duration)
            if duration < 0:
                raise ValueError
        except ValueError:
            display ('Invalid input, please enter a positive whole number.')
            duration = prompt()
            continue
        return duration

def loan_total_months(years, months):
    return (years * 12) + months

def get_apr():
    display('What is your Annual Percentage Rate, or APR?')
    user_apr = prompt('% ')

    error_message_apr = 'Invalid input, please enter a percentage out of 100%:'
    while True:
        try:
            user_apr = float(user_apr)

            if math.isnan(user_apr) or math.isinf(user_apr):
                raise ValueError
            if user_apr < 0 or user_apr > 100:
                raise ValueError
        except ValueError:
            display(error_message_apr)
            user_apr = prompt('% ')
            continue
        return user_apr / 100

def monthly_interest_rate(apr):
    return apr / 12

def calc_monthly_payment(loan, monthly_interest, duration_months):
    if monthly_interest > 0:
        monthly_payment = loan * \
            (monthly_interest / (1 - (1 + monthly_interest)\
                                 **(-duration_months)))
    else:
        monthly_payment = loan / duration_months
    return monthly_payment

def try_again():
    display('Would you like to calculate another loan repayment? y/n')
    user_answer = prompt()
    return yes_or_no(user_answer)

# Program Start #
os.system('clear')

welcome()
enter_to_continue()
os.system('clear')

while True:
    display('Loan Calculator')
    print()

    USER_LOAN = get_loan()
    DURATION_YRS, DURATION_MONTHS = get_loan_duration()
    TOTAL_DURATION = loan_total_months(DURATION_YRS, DURATION_MONTHS)
    YEARLY_APR = get_apr()
    MONTHLY_APR = monthly_interest_rate(YEARLY_APR)
    MONTHLY_REPAYMENT = \
        calc_monthly_payment(USER_LOAN, MONTHLY_APR, TOTAL_DURATION)
    print()

    display(f'Your monthly repayment for the next {DURATION_YRS} year/s and'
            f' {DURATION_MONTHS} month/s will be: ${MONTHLY_REPAYMENT:.2f}')
    print()

    if not try_again():
        break
    os.system('clear')

display('Program Terminated.')