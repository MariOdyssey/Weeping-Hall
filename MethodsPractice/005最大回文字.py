class Solution:
    def longestPalindrome(self, s):
        print(s[::-1])
        maxLen = 0
        r = ''
        for i in range(0, len(s)):
            head = s[i]
            for j in range(i, len(s)):
                til = s[j]
                if head == til and j!=i:
                    temp = s[i:j+1]
                    mask = True
                    for k in range(0, len(temp)//2):
                        if temp[k] != temp[-k-1]:
                            mask = False
                            break
                    if mask and len(temp) >= maxLen:
                        r = s[i:j+1]
                        maxLen = len(r)
        if s == '':
            r = ''
        elif r == '':
            r = s[0]
        return r


if __name__ == '__main__':
    S = Solution()
    r = S.longestPalindrome('aasssaaaaaa')
    print(r)
