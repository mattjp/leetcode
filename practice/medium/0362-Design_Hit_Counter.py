class HitCounter:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    from sortedcontainers import SortedDict # balanced BST
    self.hits = SortedDict()


  def hit(self, timestamp: int) -> None:
    """
    Record a hit.
    @param timestamp - The current timestamp (in seconds granularity).
    """
    if timestamp not in self.hits:
      self.hits[timestamp] = 0
    self.hits[timestamp] += 1


  def getHits(self, timestamp: int) -> int:
    """
    Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in seconds granularity).
    """
    hit_counter = 0
    begin_timestamp = max(timestamp-300, 0) # 5 min * 60 sec/min = 300 sec, don't look before 0
    for ts,hits in self.hits.items():
      if begin_timestamp < ts <= timestamp:
        hit_counter += hits
      elif ts > timestamp:
        break
    return hit_counter


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
