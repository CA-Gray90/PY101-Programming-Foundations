# For this practice problem, write a program that outputs The Flintstones Rock!
# 10 times, with each line prefixed by one more hyphen than the line above it.
# The output should start out like this:

string = 'The Flintstones Rock!'

# for _ in range(10):
#     string = '-' + string
#     print(string)

# LS Solution:
for padding in range(1, 11):
    print(f'{'-' * padding}{string}')