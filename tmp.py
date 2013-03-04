def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    updated = {}
    transword = getFrequencyDict(word)
    for letter in hand.keys():
        remainder = hand.get(letter,0) - transword.get(letter, 0)
        if remainder > 0:
            updated[letter] = remainder
    return updated

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

print updateHand({'a': 1, 'i': 1, 'm': 1, 'l': 2, 'q': 1, 'u': 1}, 'quail')