class Solution(object):
    def firstUniqChar(self, s):
        for i, char in enumerate(s):
            if char not in s[:i] + s[i+1:]:
                return i
        return -1


solution = Solution()

# Test Case 1
s = "loveleetcode"
output = solution.firstUniqChar(s)
print(output)

# Test Case 2
s = "leetcode"
output = solution.firstUniqChar(s)
print(output)

# Test Case 3
s = "aabb"
output = solution.firstUniqChar(s)
print(output)