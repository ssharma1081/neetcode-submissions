# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ptr2 = slow.next
        slow.next = None

        prev = None
        while ptr2:
            tmp = ptr2.next
            ptr2.next = prev
            prev = ptr2
            ptr2 = tmp

        head2 = prev

        ptr1 = head
        ptr2 = head2

        while ptr1 and ptr2:
            tmp1 = ptr1.next
            tmp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = tmp1
            ptr1 = tmp1
            ptr2 = tmp2

        
