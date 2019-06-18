import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            summ = i * i + j * j
            if summ == c:
                return True
            elif summ < c:
                i += 1
            else:
                j -= 1

        return False
