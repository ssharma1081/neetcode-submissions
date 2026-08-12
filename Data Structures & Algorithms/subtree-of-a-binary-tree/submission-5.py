# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    res = True
    answer = False
    def validateSubTree(self, root, subRoot):

        rootVal = None
        subRootVal = None

        if root:
            rootVal = root.val

        if subRoot:
            subRootVal = subRoot.val

        if rootVal != subRootVal:
            self.res = False

        if root and subRoot and (root.left or subRoot.left):
            self.validateSubTree(root.left, subRoot.left)

        if root and subRoot and (root.right or subRoot.right):
            self.validateSubTree(root.right, subRoot.right)

    def dfs(self, root, subRoot):
        if root == None:
            return
        
        if root.val == subRoot.val:
            self.res = True
            self.validateSubTree(root, subRoot)
            if self.res:
                self.answer = True

        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.dfs(root, subRoot)
        return self.answer