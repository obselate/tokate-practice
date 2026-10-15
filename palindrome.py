def is_palindrome(text):
    normalized = "".join(character for character in text if character.isalnum()).casefold()
    return normalized == normalized[::-1]
