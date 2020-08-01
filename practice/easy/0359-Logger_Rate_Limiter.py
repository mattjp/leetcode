class Logger:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.history = collections.defaultdict(set)


  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    """
    Returns true if the message should be printed in the given timestamp, otherwise returns false.
    If this method returns false, the message will not be printed.
    The timestamp is in seconds granularity.
    """            
    dt = max(0, timestamp-9)

    for i in range(dt, timestamp+1):
      if i in self.history:
        if message in self.history[i]:
          return False

    self.history[timestamp].add(message)
    return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
