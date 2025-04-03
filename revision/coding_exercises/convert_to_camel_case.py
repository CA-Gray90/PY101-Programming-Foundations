# Write a function called camel_case that converts a string with words
# separated by underscores or spaces into camel case. Your function should
# handle strings with multiple consecutive spaces or underscores appropriately.

# examples "hello_world", "first second third"
    
def camel_case(string):
    if ' ' in string:
        delimiter = ' '

    elif '_' in string:
        delimiter = '_'

    else:
        return 'Invalid String'
    
    word_list = string.split(delimiter)
    converted_words = []

    for word in word_list:
        if not converted_words:
            converted_words.append(word.lower())
        else:
            converted_words.append(word.capitalize())
    
    return ''.join(converted_words)

def camel_case(string):
    if ' ' in string or '_' in string:
        word_list = []
        word = ''

        for char in string:
            if char != ' ' and char != '_':
                word += char
            elif word:
                word_list.append(word)
                word = ''

        if word:
            word_list.append(word)
        
        print(word_list)

        converted_words = []

        for word in word_list:
            if not converted_words:
                converted_words.append(word.lower())
            else:
                converted_words.append(word.capitalize())

        return ''.join(converted_words)
    
    else:
        return 'Invalid String'
    
def camel_case(string):
    if ' ' not in string and '_' not in string:
        return string
    
    string = string.replace('_', ' ')

    words_list = string.split()
    result = []

    for word in words_list:
        if not result:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    
    return ''.join(result)


print(camel_case("hello_world") == "helloWorld")                        # True
print(camel_case("first second third") == "firstSecondThird")           # True
print(camel_case(" First seCond__    third  ") == "firstSecondThird")   # True
print(camel_case("firstSecondthird") == "firstSecondthird")             # True