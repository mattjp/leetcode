# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        Iterate through the list, create a stack of all items
        If the top is a list, push all list items to the top of the stack
        Else the top is an int and we can pop and append the int to the result
        """
        
        self.flat_list = []
        self.iter = 0
        
        stack = deque(nestedList)
        
        
        while stack:
            top = stack.popleft()
            if top.isInteger():
                self.flat_list.append(top.getInteger())
            else:
                for item in top.getList()[::-1]:
                    stack.appendleft(item)
        
    
    def next(self) -> int:
        n = self.flat_list[self.iter]
        self.iter += 1
        return n
        
    
    def hasNext(self) -> bool:
        return self.iter < len(self.flat_list)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
