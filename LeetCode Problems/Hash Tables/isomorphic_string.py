def areIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t_mapping = {}
    t_to_s_mapping = {}
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        
        # Check if s_char already has a mapping to t_char
        if s_char in s_to_t_mapping:
            if s_to_t_mapping[s_char] != t_char:
                return False
        else:
            s_to_t_mapping[s_char] = t_char
        
        # Check if t_char already has a mapping to s_char
        if t_char in t_to_s_mapping:
            if t_to_s_mapping[t_char] != s_char:
                return False
        else:
            t_to_s_mapping[t_char] = s_char
    
    return True

# Example usage:
s1 = "egg"
t1 = "add"
print(areIsomorphic(s1, t1))  # Output: True

s2 = "foo"
t2 = "bar"
print(areIsomorphic(s2, t2))  # Output: False
