# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        middle_index = len(nums) // 2
        root = TreeNode(nums[middle_index])

        root.left = self.sortedArrayToBST(nums[:middle_index])
        root.right = self.sortedArrayToBST(nums[middle_index + 1:])

        return root.val

# example 1
nums = [-10,-3,0,5,9]
output = Solution().sortedArrayToBST(nums)
print(output)

# example 2
nums = [1,3]
output = Solution().sortedArrayToBST(nums)
print(output)



