class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    
    
    def two_sum_closest(nums: List[int], t: int) -> (int, int):
      """
      return the two numbers that come closests to summing to the target `t`
      """
      
      l = 0
      r = len(nums)-1
      L = R = None
      closest = None
      while l < r:
        x = nums[l] + nums[r]
        if x == t:
          return nums[l], nums[r]
        dist = abs(t - x)
        if closest == None or dist < closest:
          closest = dist
          L = l
          R = r
        if x < t:
          l += 1
        else:
          r -= 1
      return nums[L], nums[R]
    
    
    snums = sorted(nums)
    closest = None
    for i in range(len(snums)):
      t = target - snums[i]      
      l, r = two_sum_closest(snums[:i]+snums[i+1:], t) # you can just look at `i` and beyond, no need to use entire array again
      res = l + r + snums[i]
      dist = target - res
      if closest == None or abs(dist) < abs(target-closest):
        closest = res

    return closest
