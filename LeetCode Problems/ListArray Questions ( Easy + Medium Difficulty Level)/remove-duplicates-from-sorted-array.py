class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
    
        unique_count = 1  # Initialize unique count as 1 for the first element
        current = 1  # Initialize the current index
    
        while current < len(nums):
            if nums[current] != nums[current - 1]:
                nums[unique_count] = nums[current]
                unique_count += 1
            current += 1
    
        return unique_count
    
    # Example 1:
    solution = Solution()
    nums = [1,1,2]
    print(solution.removeDuplicates(nums))  # Output: 2, nums = [1,2]

    # Example 2:
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))  # Output: 5, nums = [0,1,2,3,4]

    # Example 3:
    solution = Solution()
    nums = []
    print(solution.removeDuplicates(nums))  # Output: 0, nums = []
    