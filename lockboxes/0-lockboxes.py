#!/usr/bin/python3
"""Module that defines a function to check if all lockboxes can be opened."""


def canUnlockAll(boxes):
    """Determine whether all boxes can be unlocked.

    Args:
        boxes: a list of lists, where boxes[i] contains the keys
            found inside box i.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    if n == 0:
        return True

    unlocked = {0}
    to_visit = [0]

    while to_visit:
        current = to_visit.pop()
        for key in boxes[current]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                to_visit.append(key)

    return len(unlocked) == n
