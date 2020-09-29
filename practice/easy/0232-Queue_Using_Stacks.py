class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        
    def rebalance(self) -> None:
      if not self.s2:
        while self.s1:
          t = self.s1.pop()
          self.s2.append(t)
      

    def push(self, x: int) -> None:
      """
      Push element x to the back of queue.
      """
      self.s1.append(x)
        

    def pop(self) -> int:
      """
      Removes the element from in front of queue and returns that element.
      """
      self.rebalance()
      return self.s2.pop() # problem assumes all operations are valid
        
        

    def peek(self) -> int:
      """
      Get the front element.
      """
      self.rebalance()
      return self.s2[-1] # problem assumes all operations are valid
        

    def empty(self) -> bool:
      """
      Returns whether the queue is empty.
      """
      return len(self.s1) == 0 and len(self.s2) == 0
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
