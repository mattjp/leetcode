class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    from collections import defaultdict
    
    l, r = 0, 10
    seen = defaultdict(int)
    output = []
    while r < len(s)+1:
      window = s[l:r]
      seen[window] += 1
      if seen[window] == 2:
        output.append(window)
      r += 1
      l += 1
        
    return output
