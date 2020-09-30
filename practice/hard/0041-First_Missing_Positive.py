class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    
    # replace all nums >n or <=0 with n+1 (or any special character)
    for i in range(len(nums)):
      if nums[i] > n or nums[i] <= 0:
        nums[i] = n+1
        
    # mark each index as negative (if positive) ignoring if nums == n+1
    for i in range(len(nums)):
      j = abs(nums[i])-1
      if j < n:
        if nums[j] > 0:
          nums[j] *= -1
       
    # return index of the first positive (indicates this index is not present in the arry)
    for i in range(len(nums)):
      if nums[i] > 0:
        return i+1
      
    # otherwise, all numbers are present
    return n+1
