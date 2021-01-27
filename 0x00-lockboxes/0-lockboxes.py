#!/usr/bin/python3


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    len_boxes = len(boxes)
    if len_boxes == 0:
        return True
    for i in range(len_boxes):
        len_box = len(boxes[i])
        for x in range(1, len_box):
            if len(boxes[boxes[i][x]]) == 0 and len_boxes != i:
                return False
    return True
