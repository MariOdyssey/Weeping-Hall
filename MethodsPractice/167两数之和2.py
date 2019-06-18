class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        end = len(numbers) - 1
        while head < end:
            summ = numbers[head] + numbers[end]
            if summ == target:
                return [head + 1, end + 1]
            if summ < target:
                head += 1
            else:
                end -= 1
