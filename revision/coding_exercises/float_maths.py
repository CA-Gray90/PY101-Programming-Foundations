# Write a function that prompts the user for two floating-point numbers and
# performs the following operations on them: addition, subtraction,
# multiplication, division, floor division, modulo, and exponentiation.

# ==> Enter the first number:
# 3.5
# ==> Enter the second number:
# 2.0
# ==> 3.5 + 2.0 = 5.5
# ==> 3.5 - 2.0 = 1.5
# ==> 3.5 * 2.0 = 7.0
# ==> 3.5 / 2.0 = 1.75
# ==> 3.5 // 2.0 = 1.0
# ==> 3.5 % 2.0 = 1.5
# ==> 3.5 ** 2.0 = 12.25

# Your function should handle potential errors gracefully and ensure the input
# values are valid floating-point numbers.

def floating_operations():

    def prompt(text):
        return f'==> {text}'
    
    def valid_float(number):
        while True:
            try:
                number = float(number)
                return number
            except ValueError:
                print(prompt('Invalid Number! Try again:'))
                number = input()

    num1 = input(prompt('Enter the first number:\n'))

    num1 = valid_float(num1)

    num2 = input(prompt('Enter the second number:\n'))

    num2 = valid_float(num2)

    operation_dict = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x / y,
        '//' : lambda x, y: x // y,
        '%' : lambda x, y: x % y,
        '**' : lambda x, y: x**y
    }

    for op in operation_dict.keys():
        try:
            print(prompt(f'{num1} {op} {num2} = '
              f'{operation_dict[op](num1, num2)}'))
        except ZeroDivisionError:
            print(prompt(f'{num1} {op} {num2} = Division by Zero Error'))

floating_operations()