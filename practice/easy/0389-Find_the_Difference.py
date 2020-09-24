class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    from collections import Counter
    
    scounter = Counter(s)
    tcounter = Counter(t)
    
    for v,count in tcounter.items():
      if v not in scounter:
        return v
      elif scounter[v] != count:
        return v
      
    return ''
