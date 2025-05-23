import math
import os
import json

with open('loan_calc_messages.json', 'r') as message_file:
    MESSAGE = json.load(message_file)

MONTHS_IN_YEAR = 12

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
        display(MESSAGE['retry_yes_no'])
        answer = prompt()

def welcome():
    display(MESSAGE['welcome'])
    print()
    display(MESSAGE['explain_app'])
    print()

def enter_to_continue():
    while True:
        display(MESSAGE['enter_app'])
        input()
        break

def get_loan():
    display(MESSAGE['enter_loan'])
    loan = prompt('$')
    
    while True:
        try:
            loan = float(''.join(loan.split(',')))

            if math.isnan(loan) or math.isinf(loan) or loan <= 0:
                raise ValueError
            
            if len(str(loan).split('.')[1]) > 2:
                raise ValueError
        except ValueError:
            display(MESSAGE['invalid_loan'])
            loan = prompt('$')
            continue
        return loan
    
def get_loan_duration():
    while True:
        display(MESSAGE['enter_duration'])
        duration_years = prompt('Years: ')
        duration_years = valid_loan_duration(duration_years)

        duration_months = prompt('Months: ')
        duration_months = valid_loan_duration(duration_months)

        if (duration_months + duration_years) == 0:
            display(MESSAGE['invalid_duration_length'])
            continue
        if duration_months >= MONTHS_IN_YEAR:
            duration_years = duration_years + \
                (duration_months // MONTHS_IN_YEAR)
            duration_months = duration_months % MONTHS_IN_YEAR
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
            display (MESSAGE['invalid_duration_num'])
            duration = prompt()
            continue
        return duration

def loan_total_months(years, months):
    return (years * MONTHS_IN_YEAR) + months

def get_apr():
    display(MESSAGE['enter_apr'])
    user_apr = prompt('% ')

    while True:
        try:
            user_apr = float(user_apr)

            if math.isnan(user_apr) or math.isinf(user_apr):
                raise ValueError
            if user_apr < 0 or user_apr > 100:
                raise ValueError
        except ValueError:
            display(MESSAGE['invalid_apr'])
            user_apr = prompt('% ')
            continue
        return user_apr / 100

def monthly_interest_rate(apr):
    return apr / MONTHS_IN_YEAR

def calc_monthly_payment(loan, monthly_interest, duration_months):
    if monthly_interest > 0:
        monthly_payment = loan * \
            (monthly_interest / (1 - (1 + monthly_interest)\
                                 **(-duration_months)))
    else:
        monthly_payment = loan / duration_months
    return monthly_payment

def try_again():
    display(MESSAGE['retry_message'])
    user_answer = prompt()
    return yes_or_no(user_answer)

def main():       
    os.system('clear')

    welcome()
    enter_to_continue()
    os.system('clear')

    while True:
        display(MESSAGE['title'])
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

    display(MESSAGE['program_end'])

# Program start # 
main()