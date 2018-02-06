#!/usr/bin/env python
# -*-coding:utf-8-*-

class Array(object):
    def __init__(self, length):
        if not isinstance(length, int) and length >= 0:
            raise TypeError('{} must be int'.format(length))
        self._len = length
        self._array = [None for i in range(length)]

    def _index_judge(self, index):
        if not(isinstance(index, int) and 0 <= index < self._len):
            raise ValueError('invalid index: {}, index should in range(0, {})'
                             .format(index, self._len))

    def is_empty(self):
        return len(self._array) == 0

    def insert(self, index, obj):
        self._index_judge(index)
        self._array[index] = obj

    def delete(self, index):
        self._index_judge(index)
        self._array[index] = None

    def get(self, index):
        self._index_judge(index)
        return self._array[index]

    def find(self, obj):
        for i in range(self._len):
            if obj == self._array[i]:
                return i
        else:
            return -1


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        def check_index(r, c, row, col):
            if 0 <= r < row and 0 <= c < col:
                return True
            else:
                return False

        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if check_index(i - 1, j - 1, row, col):
                    if matrix[i - 1][j - 1] != matrix[i][j]:
                        return False
                if check_index(i + 1, j + 1, row, col):
                    if matrix[i + 1][j + 1] != matrix[i][j]:
                        return False
        return True