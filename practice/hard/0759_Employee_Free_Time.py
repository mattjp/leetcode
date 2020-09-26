"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    """
    combine all employee intervals (sorted by start time)
    combine overlapping intervals
    areas between start/end of combined intervals will be common free times
    """
    
    schedules = []
    [[schedules.append(i) for i in s] for s in schedule]
    
    schedules.sort(key=lambda i: (i.start, i.end), reverse=True) # O(1) pop
    
    combined = [schedules.pop()]
    while schedules:
      s = schedules.pop()
      c = combined.pop()
      if c.end >= s.start:
        combined.append(Interval(c.start, max(c.end, s.end)))
      else:
        combined.extend([c, s])
    
    output = []
    for i in range(1, len(combined)):
      output.append(Interval(combined[i-1].end, combined[i].start))

    return output
