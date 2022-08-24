def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase_with_no_spaces = phrase.replace(" ", "")
    
    lc_phrase_ns = phrase_with_no_spaces.lower()

    phrase_list = list(lc_phrase_ns)

    reversed_list = phrase_list.copy()
    reversed_list.reverse()

    if phrase_list == reversed_list:
        return True
    
    return False
