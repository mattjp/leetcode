class Solution:
  def trap(self, height: List[int]) -> int:
    """
    1. find the highest point behind current
    2. fill up between prev highest and current with water, ignoring land heights
    3. once max-fill has been calculated at each point, subtract land height
    """

    # save max height of water at each point
    water_heights = [0] * len(height)

    # assume highest point is 0
    prev = 0
    
    # find max water height for each point
    for i in range(1, len(height)):
        
        # we can only fill to the top of either the current or previous tallest
        water_height = min(height[i], height[prev])
        
        # update maximum water heights between the current tallest and previous tallest
        for j in range(prev+1, i):
          if water_heights[j] < water_height:
            water_heights[j] = water_height

        # update tallest point we've seen thus far
        if height[i] > height[prev]:
          prev = i

    # subtract the height of the land from the max water height at each point
    for i in range(len(water_heights)):
        water_heights[i] -= height[i]
        if water_heights[i] < 0: # don't go negative for land > water
            water_heights[i] = 0
    
    # return sum of max-fill for all points
    return sum(water_heights)
  
# redone a smarter way
class Solution:
  def trap(self, height: List[int]) -> int:
    # cannot trap if there is no bucket
    if len(height) < 3:
      return 0

    # iterate L to R
    # record maximum possible fill at each point
    # note this is monotonically increasing
    R = [height[0]]
    for i in range(1, len(height)):
      R.append(max(R[-1], height[i]))

    # same as above, but R to L
    L = [height[-1]]
    for i in range(len(height)-1, -1, -1):
      L.append(max(L[-1], height[i]))

    # reverse so indexes are the same
    L.reverse()

    # calculate the maximum fill for each index
    # maximum fill is the minimum of filling L to R and R to L
    # minus the height at that index
    max_fill = []
    for i in range(len(height)):
      max_fill.append(min(R[i], L[i]) - height[i])

    return sum(max_fill)
