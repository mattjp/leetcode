class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    curr = l = r = 0
    min_len = None
    
    while r < len(nums):
    
      while r < len(nums) and curr < s:
        curr += nums[r]
        r += 1

      while l < r and curr >= s:
        min_len = min(min_len, r-l) if min_len else r-l
        curr -= nums[l]
        l += 1
        
    return min_len if min_len else 0
