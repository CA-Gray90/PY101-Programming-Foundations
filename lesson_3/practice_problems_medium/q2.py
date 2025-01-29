# This code will fail when the input is a negative number, how can we change
# the loop so it accepts handles numbers?
# Note that we're not looking to find the factors for negative numbers, but we
# want to handle it gracefully instead of going into an infinite loop.

# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    if result:
        return result
    else:
        print('Number must be greater than zero!')

print(factors(-2))

# The purpose of number % divisor == 0 is to check whether the divisor goes into
# number evenly, and therefore is a factor of the original number passed as 
# argument to factors(). If so, then it will execute the block of code under the
# if statement.