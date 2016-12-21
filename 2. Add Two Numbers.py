# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        summation = tmp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            tmp1 = tmp2 = 0
            if l1:
                tmp1 = l1.val
                l1 = l1.next
            if l2:
                tmp2 = l2.val
                l2 = l2.next
            carry, t = divmod(tmp1 + tmp2 + carry, 10)
            tmp.next = ListNode(t)
            tmp = tmp.next
        return summation.next
