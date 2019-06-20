class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        b=[]
        for i in s:
            b.append(i)
        j = len(b) - 1
        while i < j:
            if b[i] in a and b[j] in a:
                t = b[i]
                b[i] = b[j]
                b[j] = t
                i += 1
                j -= 1
            elif not b[i] in a:
                i += 1
            elif not b[j] in a:
                j -= 1
        b = ''
        for i in s:
            b += i
        return b
