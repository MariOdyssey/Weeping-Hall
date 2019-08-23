# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == []:
            return False
        i = 0
        j = len(array[0])-1
        while i < len(array) and j >= 0:
            if target > array[i][j]:
                i += 1
            if target < array[i][j]:
                j -= 1
            if target == array[i][j]:
                return True
        return False
