class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()
        return len(s[-1])



solution = Solution()
# Example 1
s = "Hello World"
output = solution.lengthOfLastWord(s)
print(output)  # Output: 5

# Example 2
s = "   fly me   to   the moon  "
output = solution.lengthOfLastWord(s)
print(output)  # Output: 4

# Example 3
s = "luffy is still joyboy"
output = solution.lengthOfLastWord(s)
print(output)  # Output: 6