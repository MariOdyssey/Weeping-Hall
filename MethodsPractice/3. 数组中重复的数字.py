# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        newnum = numbers[:]
        for i in range(0,len(newnum)):
            newnum[i]=' '
        for i in numbers:
            if newnum[i] == i:
                duplication[0] = i
                return True
            else:
                newnum[i] = i
        return False
