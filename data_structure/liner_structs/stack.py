#!/usr/bin/env python
# -*-coding:utf-8-*-
from array import Array

class Stack(object):
    """FIFO"""
    def __init__(self, depth):
        pass

    def push(self):
        # insert
        pass

    def pop(self):
        # delete
        pass

    def is_empty(self):
        pass


"""使用一个数组实现两个堆栈

两个stack分别从数组的两头向中间生长，当两个栈顶相遇时，表示两个栈都满了
"""
class TwoStackInOneArray(object):
    ARRAY_LENGTH = 100

    def __init__(self):
        self._array = Array(self.ARRAY_LENGTH)
        # 初始化栈顶
        self.l_top = -1
        self.r_top = self.ARRAY_LENGTH

    def _check_val(self, val):
        if val is None:
            raise ValueError('items in stack should not be None')

    def push_l(self, obj):
        self._check_val(obj)
        if self.l_top + 1 == self.r_top:
            raise Exception('stack is full')
        self.l_top += 1
        self._array.insert(self.l_top, obj)

    def push_r(self, obj):
        self._check_val(obj)
        if self.r_top - 1 == self.l_top:
            raise Exception('stack is full')
        self.r_top -= 1
        self._array.insert(self.r_top, obj)

    def pop_l(self):
        if self.l_top == -1:
            raise Exception('stack is empty')
        ret = self._array.get(self.l_top)
        self._array.delete(self.l_top)
        self.l_top -= 1
        return ret

    def pop_r(self):
        if self.r_top == self.ARRAY_LENGTH:
            raise Exception('stack is empty')
        ret = self._array.get(self.r_top)
        self._array.delete(self.r_top)
        self.r_top += 1
        return ret
