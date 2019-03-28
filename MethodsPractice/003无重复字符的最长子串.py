class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempList = []
        for i in s:
            if not i in s:
                tempList.append()