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
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        if head:
            while cur.next and cur.next.next:
                if cur.next.val == cur.next.next.val:
                    tmp = cur.next.val
                    while cur.next and cur.next.val == tmp:
                        cur.next = cur.next.next
                else:
                    cur =cur.next
        return dummy.next
