#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines whether all the boxes can be opened.
    
    Args:
        boxes (list of lists): Each box is repr as a list of keys it contains.
    
    Returns:
        bool: True if all boxes can be opened, False if vice versa.
    """
    numb = len(boxes)
    unlocked = [False] * numb  # It keeps track of whether each box is unlocked
    unlocked[0] = True  # The first box will always be unlocked
    keys = set(boxes[0])  # Starts with the keys from the first box

    while keys:
        key = keys.pop()  # Selects a key
        if key < numb and not unlocked[key]:  # If it unlocks a valid and locked box
            unlocked[key] = True  # Unlocks the box
            keys.update(boxes[key])  # Add new keys from this box

    return all(unlocked)  # Check whether all boxes are unlocked

