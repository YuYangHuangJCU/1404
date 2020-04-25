import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
userinput = input('Enter a character: ').lower()


def is_valid_format(word):
    for i in word:
        if i not in VOWELS and i not in CONSONANTS:
            return False
        else:
            return True

print(is_valid_format(userinput))


word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)
