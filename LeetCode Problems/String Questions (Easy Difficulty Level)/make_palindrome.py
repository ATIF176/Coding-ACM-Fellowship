class Solution(object):
    def isPalindrome(self, s):
        stack = []
        if s == " ":
            return True
        
        for chars in s:
            if chars.isalnum():
                stack.append(chars)
        output = "".join(stack).lower()
        if output == output[::-1]:
            return True
        else:
            return False


# Example 1
solution = Solution()
s = "A man, a plan, a canal: Panama"
output = solution.isPalindrome(s)
print(output)

# Example 2
solution = Solution()
s = "race a car"
output = solution.isPalindrome(s)
print(output)

# Example 3
solution = Solution()
s = " "
output = solution.isPalindrome(s)
print(output)