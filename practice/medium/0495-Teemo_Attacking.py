class Solution:
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    from collections import deque
    from functools import reduce
    
    if len(timeSeries) == 0:
      return 0
    
    start = (timeSeries[0], timeSeries[0]+duration-1)
    intervals = deque([start]) # does not need to be a deque
    
    for ts in timeSeries[1:]:
      t = (ts, ts+duration-1)
      top = intervals.pop()
      if top[1] >= t[0]: # push overlap, if overlap
        intervals.append((top[0], t[1]))
      else: # otherwise push both
        intervals.extend([top, t])

    return reduce(lambda a,b: a+(b[1]-b[0]+1), intervals, 0) # big boi FP
