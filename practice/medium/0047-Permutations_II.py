class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    self.output = []

    def loop(nums, current) -> None:
      if len(nums) == 0:
        if current not in self.output:
          self.output.append(current.copy())
        return

      for i in range(len(nums)):
        nums_no_i = nums[:i] + nums[i+1:]
        current.append(nums[i])
        loop(nums_no_i, current)
        current.pop()

    loop(nums, [])
    return self.output
