# Write a function that takes a string argument and returns a new string that
# contains the value of the original string with all consecutive duplicate
# characters collapsed into a single character.

def crunch(string):
    result = ''

    for char in string:
        if result == '' or char != result[-1]:
            result += char

    return result

def crunch(string):
    lst = [char for char in string]

    if string:
        result = [lst[0]]
        
        for char in lst:
            if char != result[-1]:
                result.append(char)
            
        return ''.join(result)
    else:
        return string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')