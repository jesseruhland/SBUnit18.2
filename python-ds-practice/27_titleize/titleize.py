def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_list = phrase.split(" ")

    capitalized_word_list = []

    for word in word_list:
        lower = word.lower()
        lower_list = list(lower)
        lower_list[0] = lower_list[0].upper()
        new_word = "".join(lower_list)
        capitalized_word_list.append(new_word)
    
    result = " ".join(capitalized_word_list)

    return result