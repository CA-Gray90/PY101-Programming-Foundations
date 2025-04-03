# Write a program that uses loops to print a number pyramid. For example, if
# the input is 5, the output should be:

# 1
# 22
# 333
# 4444
# 55555

user_num = input('Enter a whole number greater than 1: ')

while True:
    try:
        user_num = int(user_num)
        if user_num <= 1:
            raise ValueError

    except ValueError:
        print('Please enter a whole number greater than 1: ')
        user_num = input()
    
    else:
        break

for i in range(1, user_num + 1):
    print(str(i) * i)


user_num = int(input('Enter a whole number greater than 1: '))

for i in range(1, user_num + 1):
    print(str(i) * i)