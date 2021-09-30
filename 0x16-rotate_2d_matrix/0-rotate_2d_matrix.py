#!/usr/bin/python3
"""0x16. Rotate 2D Matrix"""


def swap(matrix, i, j, param=None):
    """[summary]

    Args:
        matrix ([type]): [description]
        i ([type]): [description]
        j ([type]): [description]
        param ([type], optional): [description]. Defaults to None.
    """
    if not param:
        matrix[i][j] = matrix[i][j] * matrix[j][i]
        matrix[j][i] = matrix[i][j] // matrix[j][i]
        matrix[i][j] = matrix[i][j] // matrix[j][i]
    else:
        matrix[i][j] = matrix[i][j] * matrix[i][param]
        matrix[i][param] = matrix[i][j] // matrix[i][param]
        matrix[i][j] = matrix[i][j] // matrix[i][param]


def rotate_2d_matrix(matrix):
    """[summary]

    Args:
        matrix ([type]): [description]
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            swap(matrix, i, j)

    for i in range(len(matrix)):
        s = 0
        param = len(matrix) - 1
        while s < param:
            swap(matrix, i, s, param)
            s += 1
            param -= 1
