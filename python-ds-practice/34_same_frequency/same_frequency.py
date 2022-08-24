def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list1 = list(str(num1))
    list2 = list(str(num2))

    count1 = {}
    for num in range(9):
        count1[str(num)] = list1.count(str(num))
    
    count2 = {}
    for num in range(9):
        count2[str(num)] = list2.count(str(num))

    if count1 == count2:
        return True
    return False