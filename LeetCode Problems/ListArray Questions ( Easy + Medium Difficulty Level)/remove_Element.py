class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count, nums[:count]


# Example 1:
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
count, new_nums = solution.removeElement(nums, val)
print(count, new_nums)

# Example 2:
solution = Solution()
nums = [3,2,2,3]
val = 3
count, new_nums = solution.removeElement(nums, val)
print(count, new_nums)