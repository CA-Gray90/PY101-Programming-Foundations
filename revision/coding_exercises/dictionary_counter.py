# Write a program that counts the frequency of each character in a string and
# stores the results in a dictionary. Implement this using both a for loop and
# a while loop approach.

# PSEUDOCODE FOR LOOP:
# Set an empty dictionary; char_dict
# Iterate through the characters in the string:
# For each char in string:
#   IF char not in char_dict keys:
#       char_dict[char] = string.count(char)

# For Loop:

string = "hello world"

def for_char_counter(string):
    char_dict = {}

    for char in string:
        if char not in char_dict.keys():
            char_dict[char] = string.count(char)

    return char_dict

# While Loop:

def while_char_counter(string):
    char_dict = {}
    index = 0

    while index < len(string):
        char = string[index]

        if char not in char_dict:
            char_dict[char] = string.count(char)
        index += 1

    return char_dict


print(for_char_counter(string))
print(while_char_counter(string))

# Example:
# Input: "hello world"
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}