class MinStack:

  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = [] # (item, lowest)


  def push(self, x: int) -> None:
    lowest = self.stack[-1][1] if self.stack else x
    self.stack.append((x, min(lowest, x)))


  def pop(self) -> None:
    self.stack.pop()


  def top(self) -> int:
    return self.stack[-1][0]


  def getMin(self) -> int:
    return self.stack[-1][1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
