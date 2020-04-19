class Solution:    
  def findMaxLength(self, nums: List[int]) -> int:
    count = 0
    maxLen = 0
    counts = {}
    for n in range(0, len(nums)):
      if nums[n] == 0:
        count -= 1
      else:
        count += 1
      if count not in counts:
        counts[count] = n
      if count == 0:
        maxLen = n+1
      maxLen = max(maxLen, n - counts[count])
    return maxLen
        
  def findMaxLengthTooSlow(self, nums: List[int]) -> int:
    self.seen = set()
    self.maxLen = 0
        
    def helper(nums: List[int]) -> int:
      if len(nums) < 2:
        return self.maxLen
      if nums.count(0) == nums.count(1):
        self.maxLen = len(nums)
      return self.maxLen

      hashNums = hash(tuple(nums))

      if hashNums not in self.seen and len(nums) > self.maxLen:
        self.seen.add(hashNums)
        return max(helper(nums[1:]), helper(nums[:-1]))
      else:
        return self.maxLen

    return helper(nums) # too slow :(
    
