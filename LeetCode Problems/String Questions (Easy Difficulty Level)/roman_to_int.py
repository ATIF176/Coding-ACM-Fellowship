class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000 
        }
        total = 0
        prev_value = 0

        for c in reversed(s):
            print(c)
            value = roman_to_int[c]

            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total

solution = Solution()
s = "MCMXCIV"
output = solution.romanToInt(s)
print(output)  # Output: 1994
