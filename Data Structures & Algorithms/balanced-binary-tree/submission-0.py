# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = True
    def rec(self, root):
        if root == None:
            return 0
        
        leftHeight = self.rec(root.left)
        rightHeight = self.rec(root.right)
        if abs(leftHeight - rightHeight) > 1: 
            self.res = False

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.rec(root)
        return self.res
