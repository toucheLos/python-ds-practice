def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    ans = ''
    for ltr in phrase:
        if ltr == to_swap or ltr == to_swap.swapcase():
            ans += ltr.swapcase()
        else: 
            ans += ltr
    return ans

print(flip_case('Aaaahhh', 'h'))