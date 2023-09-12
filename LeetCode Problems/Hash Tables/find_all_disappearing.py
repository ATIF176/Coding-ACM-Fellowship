class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        # Mark the indices of numbers that appear in nums as negative
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        # Find the indices with positive values; these are the disappeared numbers
        disappeared_numbers = []
        for i in range(n):
            if nums[i] > 0:
                disappeared_numbers.append(i + 1)
        
        return disappeared_numbers


# Example usage
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))  # Output: [5, 6]

nums = [1, 1]
print(Solution().findDisappearedNumbers(nums))  # Output: [2]

nums = [1, 1, 2, 2]
print(Solution().findDisappearedNumbers(nums))  # Output: [3, 4]
