class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        min_str = min(strs, key=len)

        for i, char in enumerate(min_str):
            for s in strs:
                if s in strs:
                    if s[i] != char:
                        return min_str[:i]

        return min_str

# Example 1
input1 = ["flower", "fliw", "flight", "flw"]
solution = Solution()
output1 = solution.longestCommonPrefix(input1)
print(output1)  # Output: "fl"

# Example 2
input2 = ["dog", "racecar", "car"]
output2 = solution.longestCommonPrefix(input2)
print(output2)  # Output: ""
