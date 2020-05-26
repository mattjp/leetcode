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
  
# solved again
class Solution:  
  def findMaxLength(self, nums: List[int]) -> int:
  # map the current balance to the index at which it was seen
  # equal indicies implies an equal number of 1/0s between them

    maximum = 0
    mappings = {0: -1} # map balance to first-seen index. 0 -> -1 because 0 implies balance, -1 for 0-indexing
    balance = 0

    for i in range(len(nums)):
      if nums[i] == 1:
        balance += 1
      else:
        balance -= 1
      if balance not in mappings:
        mappings[balance] = i
      maximum = max(maximum, i - mappings[balance])

    return maximum

    
