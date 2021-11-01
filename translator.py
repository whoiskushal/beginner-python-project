# Language---> The vowel letter is converted to '9' to make a secret language.


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in 'AEIOUaeiou':
            translation = translation + str(9)
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter the phrase: ")))