class MovingAverage:

  def __init__(self, size: int):
    """
    Initialize your data structure here.
    """
    from collections import deque
    self.window = size
    self.values = deque()


  def next(self, val: int) -> float:
    self.values.append(val)
    if len(self.values) > self.window:
      self.values.popleft()
    return sum(self.values) / min(len(self.values), self.window) # if we haven't seen `window` values yet


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
