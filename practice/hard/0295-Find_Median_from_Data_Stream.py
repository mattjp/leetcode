class MedianFinder:

  def __init__(self):
    """
    initialize your data structure here.
    """
    self.min_heap = [] # right, smallest on top
    self.max_heap = [] # left, biggest on top

  def rebalance(self) -> None:
    """
    rebalance heaps if one heap gets larger than the other by >1 element
    rebalance by popping from the larger heap and pushing onto the smaller heap
    """
    if len(self.max_heap) > len(self.min_heap)+1:
      weight,x = heapq.heappop(self.max_heap)
      heapq.heappush(self.min_heap, (-weight,x))
    elif len(self.min_heap) > len(self.max_heap)+1:
      weight,x = heapq.heappop(self.min_heap)
      heapq.heappush(self.max_heap, (-weight,x))


  def addNum(self, num: int) -> None:
    """
    if `num` is larger than the current median, add to the min heap, else add to the max heap
    always rebalance
    """
    m = self.findMedian()
    if num <= m:
      heapq.heappush(self.max_heap, (-num, num))
    else:
      heapq.heappush(self.min_heap, (num, num))
    self.rebalance()  


  def findMedian(self) -> float:
    """
    return the top of the larger heap, if one exists
    otherwise return the average of the 2 heap tops
    """
    if len(self.min_heap) == len(self.max_heap) == 0:
      return 0
    elif len(self.min_heap) > len(self.max_heap):
      return self.min_heap[0][1]
    elif len(self.min_heap) < len(self.max_heap):
      return self.max_heap[0][1]
    else:
      return (self.max_heap[0][1]+self.min_heap[0][1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
