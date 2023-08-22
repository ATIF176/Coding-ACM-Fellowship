class Solution(object):
    def simplifyPath(self, path):
        components = path.split('/')
        stack = []

        for component in components:
            if component == '..':
                if stack:
                    stack.pop()
            elif component and component != '.':
                stack.append(component)

        simplified_path = '/' + '/'.join(stack)
        return simplified_path
            


solution = Solution()

# Test Case 1
path = "/home/"
output = solution.simplifyPath(path)
print(output)

path = "/../"
output = solution.simplifyPath(path)
print(output)

path = "/home//new/"
output = solution.simplifyPath(path)
print(output)