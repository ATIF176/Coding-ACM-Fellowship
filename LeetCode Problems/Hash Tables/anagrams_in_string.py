class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        
        if len(s) < len(p):
            return result
        
        # Initialize dictionaries to store character frequencies for both strings
        p_freq = {}
        s_freq = {}
        
        # Calculate character frequencies for the first window in s
        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1
        for char in s[:len(p)]:
            s_freq[char] = s_freq.get(char, 0) + 1
        
        # Slide the window through s and compare character frequencies
        for i in range(len(p), len(s)):
            if p_freq == s_freq:
                result.append(i - len(p))
            
            # Remove the leftmost character from the current window
            if s[i - len(p)] in s_freq:
                if s_freq[s[i - len(p)]] == 1:
                    del s_freq[s[i - len(p)]]
                else:
                    s_freq[s[i - len(p)]] -= 1
            
            # Add the new character to the current window
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
        
        # Check the last window
        if p_freq == s_freq:
            result.append(len(s) - len(p))
        
        return result


#example usage
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))  # Output: [0, 6]

s = "abab"
p = "ab"
print(Solution().findAnagrams(s, p))  # Output: [0, 1, 2]