class Solution:
    def __init__(self):
      self.seen = set()
    
    def loop(self, nums: List[int], maximum: int) -> int:
      if len(nums) == 0:
        return maximum
      current: int = sum(nums)
      if current > maximum:
        maximum = current
      hashable = tuple(nums)
      if hashable in self.seen:
        return maximum
      else:
        self.seen.add(hashable)
        left: List[int] = nums[1:]
        right: List[int] = nums[:-1]
        return max(self.loop(left, maximum), self.loop(right, maximum))
    
    def maxSubArray(self, nums: List[int]) -> int:
      # return self.loop(nums, sum(nums)) # too slow :(
      
      maximum: int = nums[0]
      curMax: int = nums[0]
      for i in range(1, len(nums)):
        curMax = max(nums[i], curMax + nums[i])
        if curMax > maximum:
          maximum = curMax
      return maximum
