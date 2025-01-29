# What is the difference between these two functions?

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


# The first function will mutate the original list, whereas the second one returns
# a new list object

buffer = [1, 2, 3]
print(buffer)
print(id(buffer))
add_to_rolling_buffer1(buffer, 3, 'a')

print(buffer)
print(id(buffer))

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

buffer_2 = ['a', 'b', 'c']
print(buffer_2)
print(id(buffer_2))

new_buffer = add_to_rolling_buffer2(buffer_2, 3, 'd')

print(new_buffer)
print(id(new_buffer))