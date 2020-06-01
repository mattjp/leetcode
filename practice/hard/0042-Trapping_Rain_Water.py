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
