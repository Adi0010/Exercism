from string import ascii_lowercase

a = set(ascii_lowercase)

def is_pangram(sentence):
    return set(sentence.lower()) >= a
