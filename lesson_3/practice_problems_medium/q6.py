# What will the following code output?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# 34. mess_with_it() does not reassign answer. The value of answer is immutable
# Then we assign new_answer to the return value of mess_with_it, leaving answer
# unaffected. 