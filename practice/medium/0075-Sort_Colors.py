class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # if 0 inserte at 0s pointer (iterate 1s pointer)
    # if 1, pop and insert at 1s pointer (end of ones)
    # if 2, pop and insert at end

    zeros = len(nums)-1
    ones = len(nums)-1

    for _ in range(len(nums)):
      cur = nums.pop(0)
      if cur == 0:
        nums.insert(zeros, cur)
      else:
        if cur == 1:
          nums.insert(ones, cur)
        else:
          nums.append(cur)
        ones -= 1
      zeros -= 1
      
      
# solved again
class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeros = len(nums)-1
    ones = len(nums)-1

    for _ in nums:
      top = nums.pop(0)
      if top == 0:
        nums.insert(zeros, top)
      elif top == 1:
        nums.insert(ones, top)
        zeros -= 1
      else:
        nums.append(top)
        zeros -= 1
        ones -= 1
