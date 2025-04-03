# Write a function called balanced_substrings that finds all balanced
# substrings in a given string. A balanced substring is one where:

# -  Each opening bracket has a corresponding closing bracket of the same type
# -  The brackets are properly nested (no overlapping)
# -  The function should consider (), [], and {} as valid bracket pairs

# Return a list of all balanced substrings, sorted by length (shortest first)

def balanced_substrings(string):
    substring_list = []

    for idx, char in enumerate(string):
        if char == '(':
            substring_list.append(string[idx:string.find(')', idx) + 1])
        elif char == '[':
            substring_list.append(string[idx:string.find(']', idx) + 1])
        elif char == '{':
            substring_list.append(string[idx:string.find('}', idx) + 1])

    substring_list.sort(key=len)

    return substring_list

# Refactored Code:

def balanced_substrings(string):
    substring_list = []

    for idx, char in enumerate(string):
        for k, v in {'(' : ')', '[' : ']', '{' : '}'}.items():
            if char == k:
                substring_list.append(string[idx:string.find(v, idx) + 1])

    substring_list.sort(key=len)

    return substring_list



# Example:
result = balanced_substrings("a(b)c[d]ef{g}hi(jk)") 
print(result)
# Should return: ["(b)", "[d]", "{g}", "(jk)"]

result = balanced_substrings("a(b[c{d}e]f)g")
print(result)
# Should return: ["{d}", "b[c{d}e]f", "(b[c{d}e]f)"]