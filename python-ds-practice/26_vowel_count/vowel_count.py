def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lower_phrase = phrase.lower()

    vowel_set = set('aeiou')
    phrase_list = list(lower_phrase)
    
    vowel_list = []

    result = {}

    for letter in phrase_list:
        if letter in vowel_set:
            vowel_list.append(letter)
    
    filtered_vowel_list = []

    for letter in vowel_list:
        if letter not in filtered_vowel_list:
            filtered_vowel_list.append(letter)
    
    for letter in filtered_vowel_list:
        result[letter] = 0
    
    for letter in vowel_list:
        result[letter] += 1
    
    return result