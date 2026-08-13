# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lRange = float('-inf'), rRange = float('inf')) -> bool:
        if root == None:
            return True

        if not (root.val > lRange and root.val < rRange):
            return False

        isLeftValid = self.isValidBST(root.left, lRange, root.val)
        isRightValid = self.isValidBST(root.right, root.val, rRange)

        return isLeftValid and isRightValid