class Solution(object):
    def removeDuplicateLetters(self, s):
        # Initialize variables
        stack = []
        seen = set()
        last_occurrence = {char: idx for idx, char in enumerate(s)}

        # Iterate through the characters in the string
        for idx, char in enumerate(s):
            if char not in seen:
                # Pop characters from the stack that are greater than the current character
                # and have remaining occurrences later in the string
                while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)

        return ''.join(stack)


solution = Solution()
# Test Program
s = "bcabc"
print(solution.removeDuplicateLetters(s))

# Test Program
s = "cbacdcbc"
print(solution.removeDuplicateLetters(s))
