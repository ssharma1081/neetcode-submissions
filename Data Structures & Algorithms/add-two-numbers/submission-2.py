# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        prev = ListNode()
        head = None
        while ptr1 or ptr2:
            sum = 0
            if ptr1:
                sum += ptr1.val
            if ptr2:
                sum += ptr2.val
            sum += carry
            carry = sum // 10
            newVal = sum % 10
            newNode = ListNode(newVal)
            if not head:
                head = newNode
            prev.next = newNode
            prev = newNode
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        if carry:
            newNode = ListNode(carry)
            prev.next = newNode
            
        return head
