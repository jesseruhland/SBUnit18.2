def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_set = set(nums)

    num_dict = {}

    for num in num_set:
        num_dict[num] = 0

    for num in nums:
        num_dict[num] +=1
    
    counts = list(num_dict.values())
    values = list(num_dict.keys())
    
    high_count =  max(counts)
    result_index = counts.index(high_count)

    return values[result_index]
        

