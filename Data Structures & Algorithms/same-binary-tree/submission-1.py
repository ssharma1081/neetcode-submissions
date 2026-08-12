# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = True
    def rec(self, p, q):
        pval = None
        qval = None
        if p:
            pval = p.val
        if q:
            qval = q.val
        
        if pval != qval:
            self.res = False
            return

        if p and q and (p.left or q.left):
            self.rec(p.left, q.left)

        if p and q and (p.right or q.right):
            self.rec(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.rec(p, q)
        return self.res
        
