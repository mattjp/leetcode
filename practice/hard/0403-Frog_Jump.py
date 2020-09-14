class Solution:
  def canCross(self, stones: List[int]) -> bool:
    """
    DFS
    stack = [(pos, k)]
    ex: 0,1,3,5,6,8,12,17
    [(0, 0)]
    [(-1, -1), (0, 0), (1, 1)] <- don't add combos we've seen or that are negative
    => [(1, 1)]
    [(1, 0), (2, 1), (3, 2)] <- don't go to positions that aren't stones
    => [(1, 0), (3, 2)]
    """

    stone_set = set(stones) # reachable stones, O(1)
    seen = set() # don't go to (stone,k) combos we've seen before
    target = stones[-1] # if we hit this stone, we win
    stack = [(0, 0)] # starting at stone 0
    
    while stack:
      pos,k = stack.pop() # DFS, LIFO
      if pos == target:
        return True
      if pos in stone_set: # this position is a stone
        for l in [k-1, k, k+1]: # we can make any of these 3 jumps
          if pos+l > 0 and (pos+l,l) not in seen: # don't duplicate/go backwards
            seen.add((pos+l,l))
            stack.append((pos+l,l))
            
    return False
