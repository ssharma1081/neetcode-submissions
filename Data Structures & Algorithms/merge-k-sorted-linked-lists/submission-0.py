# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val
    
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # push the head of all three lists in a minheap
        # pop the smallest and attach it, if it's next exist add it to the heap
        # keep doing this till the heap is empty
        if len(lists) == 0: 
            return None
        heap = []
        for list in lists:
            if list is not None:
                heapq.heappush(heap, NodeWrapper(list))

        head = None
        prev = ListNode()
        
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            prev.next = curr.node
            prev = curr.node
            if not head:
                head = curr.node
            if curr.node.next:
                heapq.heappush(heap, NodeWrapper(curr.node.next))

        return head
            
