#!/usr/bin/python3


def canUnlockAll(boxes):
    for i in range(len(boxes)):
        for x in range(1, len(boxes[i])):
            if len(boxes[boxes[i][x]]) == 0 and len(boxes) != i:
                return False
    return True
