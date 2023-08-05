class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in bracket_pairs.values():
                stack.append(char)
            elif char in bracket_pairs.keys():
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False
            else:
                return False
        
        return not stack

# Example 1
solution = Solution()
s = "([)]"
output = solution.isValid(s)
print(output)  # Output: False

# Example 2
solution = Solution()
s = "[](){}"
output = solution.isValid(s)
print(output)  # Output: True

# Example 3
solution = Solution()
s = "[)"
output = solution.isValid(s)
print(output)  # Output: False
