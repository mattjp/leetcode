from sortedcontainers import SortedDict

class MaxStack:
    """
    Idea: use 2 heaps
    the first heap is sorted by index. it's top element will be the top of the stack
    the second heap is sorted by value. it's top element will be the max value
    
    pushing will be O(log n) for both heaps
    peek/top is O(1) because peeking at a heap is constant time
    popping will be O(log n) because we have to pop the max element of either heap (constant)
        then we have to search and remove the element from the other heap O(log n) (binary search, rebalance)
    """

    def __init__(self):
        # keep the stack as a SortedDict sorted by position
        # index => value
        self.reg_stack = SortedDict()
        
        # keep max heap sorted by value
        # value => list of indices
        self.max_stack = SortedDict()
        
        self.counter = 0
        

    def push(self, x: int) -> None:
        self.reg_stack[self.counter] = x
        if x not in self.max_stack:
            self.max_stack[x] = []
        self.max_stack[x].append(self.counter)
        self.counter += 1
        

    def pop(self) -> int:
        index, value = self.reg_stack.popitem()
        indices = self.max_stack[value]
        if len(indices) == 1:
            self.max_stack.pop(value)
        else:
            self.max_stack[value] = indices[:-1]  # remove the most recently added
        return value
        

    def top(self) -> int:
        return self.reg_stack.peekitem()[1]  # peekitem returns (index, value)

    
    def peekMax(self) -> int:
        return self.max_stack.peekitem()[0]  # peekitem returns (value, indices)

    
    def popMax(self) -> int:
        value, indices = self.max_stack.peekitem()
        
        index = indices[-1]
        indices.pop()
        
        if len(indices) == 0:
            self.max_stack.popitem()
        else:
            self.max_stack[value] = indices
        
        self.reg_stack.pop(index)
        return value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
