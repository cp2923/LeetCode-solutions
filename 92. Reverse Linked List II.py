# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while i < m:
            pre = pre.next
            i += 1
        reverse = None
        cur = pre.next
        while i < n + 1:
            tmp = cur.next
            cur.next = reverse
            reverse = cur
            cur = tmp
            i += 1

        pre.next.next = cur
        pre.next = reverse

        return dummy.next
