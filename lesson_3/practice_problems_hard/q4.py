def is_an_ip_number(string):
    try:
        int(string)
    except ValueError:
        return False
    
    return int(string) in range(0, 256)

# LS function:
# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    IP_LENGTH = 4 
    if len(dot_separated_words) != IP_LENGTH:  # Check length of list (4 elements)
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    if dot_separated_words:                    # check if list is empty, then return True
        return False
    return True

# LS Solution:

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     IP_LENGTH = 4 
#     if len(dot_separated_words) != IP_LENGTH:  # Check length of list (4 elements)
#         return False
    
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             return False                      # Instead of break, just return False. Duuuuhhhhhhh

#     return True


# Should all print True
print(is_dot_separated_ip_address('4.3.2') == False)
print(is_dot_separated_ip_address('4.3.2.5.7') == False)
print(is_dot_separated_ip_address('4.3.2.5') == True)
print(is_dot_separated_ip_address('4.3.2.xa') == False)
print(is_dot_separated_ip_address('4.3.csd.45') == False)
print(is_dot_separated_ip_address('4.3.255.0') == True)
print(is_dot_separated_ip_address('1.023874.12314.45') == False) 


# print(is_an_ip_number('10'))     # True
# print(is_an_ip_number('255')) # True
# print(is_an_ip_number('0'))  # True
# print(is_an_ip_number('256'))    # False
# print(is_an_ip_number('-10'))    # False
# print(is_an_ip_number('1.5'))    # False