"""Module that provides is_palindrome.

Author of is_palindrome: Allison Patterson
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns True if a word is a palindrome.

    word: string
    """

    rest = middle(word)
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(rest)
