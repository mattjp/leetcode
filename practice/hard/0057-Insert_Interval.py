class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    - since `intervals` is sorted by start time, simply insert newInterval (sorted).
    - then iterate through `intervals` combining any overlapping intervals.
    - this is done by popping from `intervals`.
    """
    
    # since `intervals` is sorted, we only need to check this one overlap.
    def overlaps(a_end, b_start):
      if a_end >= b_start:
        return True
      return False
    

    # insert `newInterval`.
    i = 0
    while i < len(intervals) and intervals[i][0] < newInterval[0]:
      i += 1
    intervals.insert(i, newInterval)
    
    # compare the top of `output` with the bottom of `intervals`
    output = [intervals.pop(0)]
    while intervals:
      i = intervals.pop(0)
      o = output.pop()
      if overlaps(o[1], i[0]): # if there is overlap, create and append the new overlap interval
        n = [min(i[0], o[0]), max(i[1], o[1])]
        output.append(n)
      else:
        output.extend([o, i])
        
    return output
