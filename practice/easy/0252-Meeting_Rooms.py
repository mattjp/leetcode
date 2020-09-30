class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    from collections import deque
    
    sorted_intervals = deque(sorted(intervals, key=lambda i: (i[0], i[1])))
      
    for i in range(1, len(sorted_intervals)):
      l = sorted_intervals[i-1]
      r = sorted_intervals[i]
      
      if r[0] < l[1]:
        return False
      
    return True
