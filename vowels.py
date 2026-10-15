def count_vowels(text):
    return sum(char in "aeiou" for char in text.lower())
