
class Solution(object):
    def dect(self, i,j,s):
        while i<j:
            if not s[i] == s[j]:
                return False
            j -= 1
            i += 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        mark = 0
        m=True
        while i < j and mark < 2:
            if not s[i] == s[j]:
                m=False
                mark += 1
                if self.dect(i + 1, j, s) | self.dect(i, j - 1, s):
                    m = True
        return m
