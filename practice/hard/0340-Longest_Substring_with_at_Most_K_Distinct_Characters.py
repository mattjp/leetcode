class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    """
    sliding window
    stop iterating r pointer when there are more than k distinct chars
    stop iterating l pointer when there are exactly k distinct chars
    """
    from collections import defaultdict
    
    distinct = defaultdict(int)
    longest = l = r = 0
    
    if k == 0:
      return 0
    
    while r < len(s):
      while r < len(s):
        distinct[s[r]] += 1
        if len(distinct) > k: # break here so that r is not 2 past end
          break
        r += 1

      longest = max(longest, r-l) # r is going to be 1 past end of longest

      while l < r and len(distinct) > k: # worked the same for l<r and l<=r
        distinct[s[l]] -= 1
        if distinct[s[l]] == 0:
          distinct.pop(s[l])
        l += 1 # note that we don't break here, because l is inclusive (r is exclusive)

      r += 1 # always move r to add next letter (since prev r was already added)
      
    return longest
