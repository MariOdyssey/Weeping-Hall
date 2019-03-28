class Solution:
    def bucketSort(self, nums):
        # 选择一个最大的数
        max_num = max(nums)
        # 创建一个元素全是0的列表, 当做桶
        bucket = [0] * (max_num + 1)
        # 把所有元素放入桶中, 即把对应元素个数加一
        for i in nums:
            bucket[i] += 1

        # 存储排序好的元素
        sort_nums = []
        # 取出桶中的元素
        for j in range(len(bucket)):
            if bucket[j] != 0:
                for y in range(bucket[j]):
                    sort_nums.append(j)
        return sort_nums

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = self.bucketSort(nums)
        i = 0
        j = len(nums)-1
        while i != j:
            if nums[i]+nums[j] == target:
                return [i, j]
            elif nums[i]+nums[j] > target:
                j = j - 1
            else:
                i = i + 1
