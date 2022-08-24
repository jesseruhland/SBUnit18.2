def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = list(phrase)

    phrase_list.reverse()

    reversed_phrase = ''.join(phrase_list)

    return reversed_phrase