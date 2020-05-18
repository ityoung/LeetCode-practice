# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            depth = max(l, r) + 1
        return depth