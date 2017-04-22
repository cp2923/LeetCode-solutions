# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        newHead = ListNode(0)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        new = newHead
        while current.next:
            if current.next.val < x:
                new.next = current.next
                current.next = current.next.next
                new = new.next
            else:
                current = current.next
        new.next = dummy.next
        return newHead.next
