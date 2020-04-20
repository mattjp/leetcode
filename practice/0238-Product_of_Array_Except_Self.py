class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    L = [1] * len(nums) # L[0] should be 1, since there is nothing to the left of nums[0]
    R = [1] * len(nums) # R[-1] should be 1, since there is nothing to the right of nums[-1]
    for n in range(1, len(nums)): # iterate L -> R storing product of nums left of index 
      L[n] = L[n-1] * nums[n-1]
    for n in range(len(nums)-2, -1, -1): # iterate R -> L storing product of nums right of index
      R[n] = R[n+1] * nums[n+1]
    return list(map(lambda l, r: l * r, L, R))
