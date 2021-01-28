#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened
    """
    array = [0]
    len_boxes = len(boxes)
    if (len_boxes == 0):
        return True
    for key in array:
        for key_box in boxes[key]:
            if key_box not in array and key_box < len_boxes:
                array.append(key_box)
    if len(array) == len_boxes:
        return True
    return False
