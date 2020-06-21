class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:

    # given interval 1 starts before interval 2, return True if they overlap
    def overlaps(i1: List[int], i2: List[int]) -> bool:
      return i2[0] < i1[1]

    # sort by start time, secondary sort by end time
    sorted_intervals = sorted(intervals, key=lambda i: (i[0], i[1]))

    # dumb edge case
    if len(sorted_intervals) < 1:
      return 0

    # use priority queue of intervals, sorted by earliest end time
    pq = [(sorted_intervals[0][1], sorted_intervals[0])]
    min_rooms = 1

    for interval in sorted_intervals[1:]:
      # until there is an overlap, we can keep popping meetings off of the PQ
      # we pop the earliest-ending meeings
      while pq and not overlaps(pq[0][1], interval):
        heapq.heappop(pq)
      # once there is an overlap, we add the current meeting to the PQ
      heapq.heappush(pq, (interval[1], interval))
      min_rooms = max(min_rooms, len(pq))

    return min_rooms
