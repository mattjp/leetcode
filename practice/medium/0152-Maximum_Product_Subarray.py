class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    mmin = nums[0] # smallest current subarray product
    mmax = nums[0] # largest current subarray product
    output = nums[0]
    
    for n in nums[1:]:
      # new mmax/mmin will either start at `n` or be a product of previous min or max
      x = min(n, mmin*n, mmax*n)
      y = max(n, mmin*n, mmax*n)
      mmin = x
      mmax = y
      output = max(output, mmax)
    
    return output
