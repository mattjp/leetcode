class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # sort by interval start, reversed
    # this allows for O(1) pop/push
    sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=True)

    output = []

    while len(sorted_intervals) > 1:
      # compare the two smallest intervals
      sm = sorted_intervals.pop()
      lg = sorted_intervals.pop()
      # if there is overlap, re-append the resulting overlap interval
      if sm[1] >= lg[0]:
        l = min(sm[0], lg[0])
        r = max(sm[1], lg[1])
        sorted_intervals.append([l,r])
      # otherwise the smallest interval can be appended to the output
      else:
        output.append(sm)
        sorted_intervals.append(lg)

    # take care of the remaining interval, if one exists
    if len(sorted_intervals) > 0:
      output.append(sorted_intervals[0])

    return output
