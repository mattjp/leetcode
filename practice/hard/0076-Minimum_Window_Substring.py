class Solution:
  def minWindow(self, s: str, t: str) -> str:
    from collections import Counter
    
    t_counter = Counter(t)
    s_counter = Counter()
    
    n = len(t_counter)
    best = ''
    l = r = m = 0
    
    # outer loop - perform 1 and 2 until r is at the end of s
    while r < len(s):
    
      # step 1: inc r until all counts are high enough (now in valid state)
      while r < len(s) and m < n:
        ch = s[r]
        if ch in t_counter:
          s_counter[ch] += 1
          if s_counter[ch] == t_counter[ch]:
            m += 1
        r += 1
    
      # step 2: inc l until 1 count dips below threshold (now in invalid state)
      while l < r and m == n:
        # at the start of each loop, we know s[l:r] is valid,
        # so we check to see if this substring is smallest
        if best == '' or len(best) > len(s[l:r]):
          best = s[l:r]
        ch = s[l]
        if ch in t_counter:
          s_counter[ch] -= 1
          if s_counter[ch] < t_counter[ch]:
            m -= 1
        l += 1
      
    return best
