# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxx = float('-inf')):
            nonlocal res
            if not root:
                return
            maxx = max(root.val, maxx)
            dfs(root.left, maxx)
            dfs(root.right, maxx)
            if root.val >= maxx:
                res += 1
        dfs(root)
        return res

        