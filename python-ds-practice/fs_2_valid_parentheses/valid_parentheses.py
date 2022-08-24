def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    length = len(parens)
    
    if length % 2 != 0:
        return False

    half_length = int(length/2)

    if parens[0] == ')' or parens[-1] == '(':
        return False
    
    first_half = parens[:half_length]

    first_translated = first_half.replace('(', "l")
    first_final = first_translated.replace(')', "r")

    first_list = list(first_final)  

    second_half = parens[half_length:]

    second_translated = second_half.replace('(', "r")
    second_final = second_translated.replace(')', "l")


    second_list = list(second_final)

    second_list.reverse()


    if first_list == second_list:
        return True
    
    return False

    
    
