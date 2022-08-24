def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_list = list(phrase)

    result_dict = {}
    
    for letter in letter_list:
        result_dict[letter] = 0

    for char in phrase:
        result_dict[char] +=1
    
    return result_dict