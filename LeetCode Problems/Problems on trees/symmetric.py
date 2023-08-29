# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left_root, right_root):
        if left_root is None and  right_root is None:
            return True
        elif ((left_root is None) != (right_root is None)):
            return False
        else:
            return (left_root.val == right_root.val) and self.isMirror(left_root.left, right_root.right) and self.isMirror(left_root.right, right_root.left)


# example 1
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# example 2
# Input: root = [1,2,2,null,3,null,3]
# Output: false

