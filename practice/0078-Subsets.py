class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    self.result = []

    def loop(nums: List[int], current: List[int]) -> None:
      if current not in self.result:
        self.result.append(current.copy()) # copy because lists are mutable
      for i in range(len(nums)):
        current.append(nums[i])
        loop(nums[i+1:], current)
        current.pop() # remove this digit once we've tried all permutations

    loop(nums, [])
    return self.result
