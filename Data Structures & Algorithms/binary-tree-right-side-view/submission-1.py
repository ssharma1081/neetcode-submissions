# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = []

    def dfs(self, root, d = 0):
        if not root:
            return None
        if d == len(self.res):
            self.res.append([])

        self.dfs(root.left, d + 1)
        self.dfs(root.right, d + 1)
        self.res[d].append(root.val)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return list(l[-1] for l in self.res)

        