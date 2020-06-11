class Solution:  
    def __init__(self):
      self.output = set()
      self.seen = set()
  

    def twoSum(self, nums: List[int], target: int) -> None:
      """
      requires nums to be sorted
      does the basic 2-pointer approach
      """
      l = 0
      r = len(nums)-1
      while l < r:
        t = nums[l] + nums[r]
        if t == target:
          o = tuple(sorted([nums[l], -target, nums[r]])) # no duplicates
          if o not in self.output:
            self.output.add(o)
          l += 1
          r -= 1
        elif t > target:
          r -= 1
        else:
          l += 1


    def threeSum(self, nums: List[int]) -> List[List[int]]:
      sort_nums = sorted(nums) # sort first to enable 2-pointer 2-sum
      for i,num in enumerate(sort_nums):
        tmp_nums = sort_nums[:i] + sort_nums[i+1:]
        if tuple(tmp_nums) not in self.seen: # don't look at arrays we've seen before
          self.seen.add(tuple(tmp_nums))
          self.twoSum(tmp_nums, -num)
        
      return list(self.output)
