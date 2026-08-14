# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0

        mp = {val: index for index, val in enumerate(inorder)}
        
        def dfs(l, r):
            if l > r:
                return None

            root = TreeNode(preorder[self.pre_idx])
            mid = mp[root.val]
            self.pre_idx += 1

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)