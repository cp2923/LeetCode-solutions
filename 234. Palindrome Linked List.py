# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return True
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l = l + 1
        half = l / 2
        i = 0
        cur = head
        pre = None
        while i < half:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            i += 1
        if l % 2 != 0:
            cur = cur.next
        while cur:
            if pre.val != cur.val:
                return False
            pre = pre.next
            cur = cur.next

        return True
