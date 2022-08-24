def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    vowel_list = []

    for char in s:
        if char in vowel_set:
            vowel_list.append(char)
    
    vowel_list.reverse()

    char_list = []

    for char in s:
        if char not in vowel_set:
            char_list.append(char)
        elif char in vowel_set:
            char_list.append(vowel_list[0])
            vowel_list.pop(0)
    
    result_string = "".join(char_list)

    return result_string


