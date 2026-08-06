# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow = head
        fast = head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1

        if not fast:
            if slow.next == None:
                head = None
            else:
                head = head.next
            return head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return head
