# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        ptr = head
        prev = None
        while ptr:
            # if ptr.next == None:
            #     break
            print(ptr.val)
            tmp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = tmp
        return prev