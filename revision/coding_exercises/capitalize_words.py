# Write a function that takes a string and returns a string with all the words
# first letters capitalized and the others remaining as thier original case

def capitalize_words(sentence):
    word_list = sentence.split()
    return ' '.join(word[0].upper() + word[1:] for word in word_list)

s = 'this iS a senTence without caPital leTTers at THE starT of eAch WoRD'

print(capitalize_words(s))