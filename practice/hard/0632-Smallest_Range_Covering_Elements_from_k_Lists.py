class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    from collections import deque

    heap = []
    nums = [deque(nums[i]) for i in range(len(nums))] # make deque so we can popleft
    largest = None
    
    for i,num in enumerate(nums):
      heap.append((num.popleft(), i)) # take smallest element from every `num`
      if not largest or heap[-1][0] > largest: # maintain `largest` on every insertion
        largest = heap[-1][0]
    heapq.heapify(heap) 
    
    best = None
    smallest_dist = None
    
    # when one num runs out of ints, stop iteration
    # this isn't very safe, but whatever
    while True:
      smallest, i = heapq.heappop(heap) # calculate the distance from the top of the heap to the largest element
      dist = abs(largest-smallest)
      if smallest_dist == None or dist < smallest_dist:
        smallest_dist = dist
        best = [smallest, largest]
        
      # once we have seen all ints in a `num`, and the int from that `num` was the smallest in the heap, we can stop
      if not nums[i]: 
        break

      num = nums[i].popleft() # take next smallest thing from `num` of the smallest heap element
      heapq.heappush(heap, (num,i))
      largest = max(largest, num)

    return best
