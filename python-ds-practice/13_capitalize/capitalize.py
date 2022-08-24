def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase_list = list(phrase)

    capital_letter = phrase_list[0].upper()

    phrase_list[0] = capital_letter

    result = "".join(phrase_list)

    return result