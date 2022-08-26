class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        1. Use l and r pointer
        2. Use set and map to keep track of chars
        """
        
        l = ans = 0
        
        distinct = set()
        counts = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        
        for r in range(len(s)):
            counts[s[r]] += 1
            if s[r] not in distinct:
                distinct.add(s[r])
            
            while len(distinct) == 3:
                # if the prefix contains all the required chars, then all suffixes
                # will count as valid
                ans += len(s) - r
                
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    distinct.remove(s[l])
                l += 1
                
        return ans
