# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def preOrder(root):
            nonlocal res
            if root == None:
                return
            
            preOrder(root.left)
            if len(res) < k:
                res.append(root.val)
            preOrder(root.right)

        preOrder(root)

        return res[-1]