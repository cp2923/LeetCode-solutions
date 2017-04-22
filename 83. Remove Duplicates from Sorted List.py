# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        if cur:
            while cur.next:
                if cur.next.val == cur.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
        return head
