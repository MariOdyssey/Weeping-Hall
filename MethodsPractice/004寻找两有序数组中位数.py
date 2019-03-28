class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        j = 0
        if nums2 == []:
            pass
        elif nums1==[]:
            nums1 = nums2
        else:
            for i in nums2:
                if i <= nums1[0]:
                    nums1.insert(0, i)
                    continue
                while j < len(nums1)-1:
                    left = nums1[j]
                    right = nums1[j + 1]
                    if i > left and i <= right:
                        nums1.insert(j+1, i)
                        break
                    else: j += 1
                if i > nums1[-1]:
                    nums1.append(i)

        if len(nums1)%2 == 0:
            k = int(len(nums1)/2)-1
            return (nums1[k] + nums1[k+1])/2.0
        else:
            return nums1[int(len(nums1)/2)]*1.0


if __name__ == '__main__':
    a = [1, 2, 4]
    b = [3]
    c = Solution()
    d = c.findMedianSortedArrays(a, b)
    print(d)