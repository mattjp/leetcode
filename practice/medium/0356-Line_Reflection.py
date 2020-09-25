class Solution:
  def isReflected(self, points: List[List[int]]) -> bool:
    from collections import defaultdict
    
    ys = defaultdict(list)
    
    for x,y in points:
      if x not in ys[y]:
        ys[y].append(x)
      
    reflect = None
    
    # this is unecessary, just the furthest left point and the furtherest right point
    # will get you the reflection line, but doing it this way leads to early termination.
    for xs in ys.values():
      mean = sum(xs) / len(xs)
      if not reflect:
        reflect = mean
      elif mean != reflect:
        return False
      
    for xs in ys.values():
      for x in xs:
        d = abs(reflect-x)
        if d+reflect not in xs:
          return False
    return True
