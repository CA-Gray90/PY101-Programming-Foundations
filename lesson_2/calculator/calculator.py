def prompt(message):
    print(f'==> {message}')

prompt('Welcome to Calculator!')

prompt("What's the first number?")
num_1 = input()

prompt("What's the second number?")
num_2 = input()

prompt(
    ('What operation would you like to perform?\n'
    '1) Addition, 2) Subtraction, 3) Multiplication, 4) Division')
)
operation = input()

match operation:
    case '1':
        result = int(num_1) + int(num_2)
    case '2':
        result = int(num_1) - int(num_2)
    case '3':
        result = int(num_1) * int(num_2)
    case '4':
        result = int(num_1) / int(num_2)

prompt(f'The result is {result}')