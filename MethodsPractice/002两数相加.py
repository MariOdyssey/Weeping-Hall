# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2) -> int:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        remainder = 0
        for i in range(max(len(l1), len(l2))):
            if not l1[i]==None or l2[i]==None:
                l3.append((l1[i] + l2[i]) % 10 + remainder)
                remainder = (l1[i] + l2[i])//10
            if l1[i]==None:
                l3.append(l2[i] + remainder)
                remainder = 0
            if l2[i] == None:
                l3.append(l1[i] + remainder)
                remainder = 0
            if i == max(len(l1), len(l2)) and l1[i]!=None and l2[i]!=None:
                l3.append((l1[i] + l2[i]) % 10 + remainder)
                l3.append((l1[i] + l2[i])//10)
        return l3
