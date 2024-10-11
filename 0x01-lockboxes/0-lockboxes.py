#!/usr/bin/python3


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)