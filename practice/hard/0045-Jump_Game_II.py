class Solution:
  def jump(self, nums: List[int]) -> int:
    """
    BFS using queue?
    if this is too slow, use a heap?
    """
    
    from collections import deque
    
    queue = deque([(0, 0)]) # (index, jumps)
    visited = {} # index -> jumps, can also just be a set of (index, jumps)
    n = len(nums)-1
    
    while queue:
      i, jumps = queue.popleft()
      if i >= n:
        return jumps
      
      for j in range(nums[i], 0, -1):
        if j+i >= n:
          return jumps+1
        if j+i not in visited or visited[j+i] > jumps:
          visited[j+i] = jumps
          queue.append((j+i, jumps+1))
          
    return -1
