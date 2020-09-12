class Solution:
  def connectSticks(self, sticks: List[int]) -> int:
    if len(sticks) < 1:
      return 0
    
    heap = sticks.copy()
    heapq.heapify(heap)
    output = []
    
    while len(heap) > 1:
      x = heapq.heappop(heap) + heapq.heappop(heap)
      output.append(x)
      heapq.heappush(heap, x)

    return sum(output)        
