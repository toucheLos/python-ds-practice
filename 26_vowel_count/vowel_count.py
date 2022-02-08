def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    new = phrase.lower()
    count = {}
    vowels = 'aeiou'
    for vowel in vowels:
        for letter in new:
            if vowel == letter:
                count[letter] = count.get(letter, 0) + 1
    return count

print(vowel_count('HOW ARE YOU? i am great!') )
