# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        

# example 1
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# example 2
# Input: root = []
# Output: []

# example 3                                                                 
# Input: root = [1]
# Output: [1]
