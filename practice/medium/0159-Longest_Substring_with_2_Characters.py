class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        distinct = {}
        dist = 0
        r = l = 0
        
        for r in range(len(s)):
            if s[r] in distinct:
                distinct[s[r]] += 1
            else:
                distinct[s[r]] = 1
                while len(distinct) > 2:
                    """
                    0123456
                    ccaabbb
                    l   r
                      l r
                      l   r
                    """
                    # dist is l to r, not including r
                    dist = max(dist, r-l)
                    
                    distinct[s[l]] -= 1
                    if distinct[s[l]] == 0:
                        distinct.pop(s[l])
                    l += 1

        # Check to see if the last substring is the solution
        # R+1 because the length is 0-indexed
        return max(dist, r+1 - l)
