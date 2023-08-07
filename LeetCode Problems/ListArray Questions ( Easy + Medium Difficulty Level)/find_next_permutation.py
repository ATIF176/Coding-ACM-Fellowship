class Solution(object):
    def nextPermutation(self, nums):
        # Find the first element from the right that is smaller than the element to its right
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If no such element is found, the array is in descending order, so reverse it to get the lowest order
        if i == -1:
            nums.reverse()
            return

        # Find the smallest element to the right of i that is larger than nums[i]
        j = len(nums) - 1
        while j>= 0 and nums[j] <= nums[i]:
            j -= 1
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements to the right of i to get the next lexicographical permutation
        nums[i+1:] = reversed(nums[i+1:])


solution = Solution()
# Test cases
nums1 = [1, 2, 3]
solution.nextPermutation(nums1)
print(nums1)  # Output: [1, 3, 2]

nums2 = [3, 2, 1]
solution.nextPermutation(nums2)
print(nums2)  # Output: [1, 2, 3]

nums3 = [1, 1, 5]
solution.nextPermutation(nums3)
print(nums3)  # Output: [1, 5, 1]
