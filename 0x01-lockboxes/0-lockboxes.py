#!/usr/bin/python3
"""LOckboxes challenge"""


def canUnlockAll(boxes):
    """
    It determines if all the boxes can be opened.

    :param boxes: A list of lists, where each inner list contains keys to other boxes
    :return: True if all boxes can be opened, False otherwise
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
                if len(unlocked) == len(boxes):
                    return True
    return len(unlocked) == len(boxes)
