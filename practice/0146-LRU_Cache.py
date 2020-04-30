class LRUCache:

  def __init__(self, capacity: int):
    self.key_values = {}
    self.most_recent = []
    self.capacity = capacity
    self.weight = 0

  def update_most_recent(self, key: int) -> None:
    self.most_recent = list(map(lambda x: (self.weight, x[1]) if x[1] == key else x, self.most_recent))
    self.most_recent.sort()
    self.weight += 1

  def get(self, key: int) -> int:
    if key in self.key_values:
      self.update_most_recent(key)
      return self.key_values[key]
    return -1

  def put(self, key: int, value: int) -> None:
    if len(self.most_recent) == self.capacity:
      if key not in self.key_values:
        (_, most_recent_key) = heapq.heappop(self.most_recent)
        del self.key_values[most_recent_key]
        self.key_values[key] = value
        heapq.heappush(self.most_recent, (self.weight, key))
        self.weight += 1
      else:
        self.update_most_recent(key)
        self.key_values[key] = value
    else:
      if key not in self.key_values:
        self.key_values[key] = value
        heapq.heappush(self.most_recent, (self.weight, key))
        self.weight += 1
      else:
        self.update_most_recent(key)
        self.key_values[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
