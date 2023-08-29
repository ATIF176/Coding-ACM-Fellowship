# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        # Assuming you're comparing node values
        if p.val != q.val:
            return False
        
        # Recursive calls for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# example 1
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# example 2
# Input: p = [1,2], q = [1,null,2]
# Output: false

# example 3
# Input: p = [1,2,1], q = [1,1,2]
# Output: false