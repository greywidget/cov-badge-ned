"""Just some random string functions for testing coverage"""

from string import ascii_letters, punctuation

DISCARD = punctuation + "".join([str(num) for num in range(10)])


def get_words(sentence: str, title_case: bool = False):
    """Return a list of words, excluding punctuation"""
    table = sentence.maketrans("", "", punctuation)
    words = sentence.translate(table).split()

    if title_case:
        words = [word.title() for word in words]

    return words


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    text = "".join(letter for letter in text if letter not in DISCARD)

    return [
        word
        for word in text.split()
        if word.lower()
        != ("".join(letter for letter in word.lower() if letter in ascii_letters))
    ]
