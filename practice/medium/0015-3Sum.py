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


# solved again using hash map approach
class Solution:
  def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
    seen = set()
    output_set = set()
    output = []
    for num in nums:
      if target-num in seen:
        res = sorted([num, target-num, -target])
        if repr(res) not in output_set:
          output.append(res)
          output_set.add(repr(res))
      else:
        seen.add(num)
    return output
    
  
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    seen = set()
    seen_nums = set()
    output_set = set()
    output = []
    for i,num in enumerate(nums):
      if num in seen_nums:
        continue
      seen_nums.add(num)
      
      nums_i = nums[i+1:] # we don't have to check before `i` - prior combinations have been checked
      if repr(nums_i) in seen:
        continue
      seen.add(repr(nums_i))

      res = self.two_sum(nums_i, -num)
      for r in res:
        if repr(r) not in output_set:
          output.append(r)
          output_set.add(repr(r))

    return output
