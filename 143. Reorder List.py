# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        p1 = head
        p2 = head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        mid = p1.next
        p1.next = None # must set to None, otherwise the result would have a cycle

        # reverse second half
        pre = None
        cur = mid
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        q = pre
        p = head
        while p and q:
            tmp = q.next
            q.next = p.next
            p.next = q

            p = p.next.next
            q = tmp
