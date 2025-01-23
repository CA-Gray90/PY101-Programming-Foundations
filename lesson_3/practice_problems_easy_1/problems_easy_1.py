# Practice Problems: Easy 1 Solutions here:

# Q1: Will this code raise an error:
# numbers = [1, 2, 3]
# numbers[6] = 5

# A: Yes, on line 5 we attempt to access an index that does not exist (IndexError)

# Q2: How can you determine whether a given string ends with an exclamation mark (!)?
# Write some code that prints True or False depending on whether the string ends with an exclamation mark.

# def ends_with_exclamation(string):
#     print(string[-1] == '!')

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# ends_with_exclamation(str1)
# ends_with_exclamation(str2)

# LS Solution: using .endswith() method. i.e str1.endswith('!')

# Q3: Show two different ways to create a new string with "Four score and " 
# prepended to the front of the string referenced by famous_words.

# famous_words = "seven years ago..."

# new_string = "Four score and " + famous_words
# print(famous_words)

# new_string = ''.join(["Four score and ", famous_words])
# print(new_string)

#L.S solution: String interpolation:
# new_string = f'Four score and {famous_words}'
# print(new_string)

# Q4: Using the following string, print a string that contains the same value, 
# but using all lowercase letters except for the first character, which should be capitalized.

# munsters_description = "the Munsters are CREEPY and Spooky."

# print(munsters_description.lower().capitalize())
# The .lower() method is unnecessary as .capitalize capitalizes the first character and lowers all else

# Q5: print the string with the case of all letters swapped:

# munsters_description = "The Munsters are creepy and spooky."

# print(munsters_description.swapcase())

# Q6: Determine whether the name Dino appears in the strings below -- check each string separately:
# def check_for_dino(string):
#     return False if string.find('Dino') == -1 else True

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print(check_for_dino(str1))
# print(check_for_dino(str2))

# or:
# def check_for_dino2(string):
#     return 'Dino' in string

# print(check_for_dino2(str1))
# print(check_for_dino2(str2))

# Q7
# How can we add the family pet, "Dino", to the following list?

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# flintstones.append('Dino')
# flintstones += ['Dino']
# flintstones.extend(['Dino'])
# flintstones.insert(0, 'Dino')
# print(flintstones)

# Q8: How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')?
# Replace the call to append with another method invocation.

# flintstones.extend(['Dino', 'Hoppy'])
# print(flintstones)

# Q9: Print a new version of the sentence given by advice that ends just before
# the word house. Don't worry about spaces or punctuation: remove everything
# starting from the beginning of house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."

# print(advice.index('house'))
print(advice[:advice.index('house')])

# LS solution uses .split('house'):
print(advice.split("house")[0])
print(advice.split("house"))

# This returns a list with two elements, both being either part of the sentence
# split or seperated by "house", then printing the first element of that list.

# Q10: Print the following string with the word important replaced by urgent:

advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace("important", "urgent"))