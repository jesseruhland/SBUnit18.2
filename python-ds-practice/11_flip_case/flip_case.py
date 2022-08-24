def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_list = list(phrase)

    result_list = []

    for letter in phrase_list:
        if letter.lower() == to_swap.lower():
            new_val = letter.swapcase()
            result_list.append(new_val)
        elif letter.lower() != to_swap.lower():
            result_list.append(letter)
    
    result = "".join(result_list)

    return result