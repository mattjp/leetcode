class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:

    def binarySearch(nums: List[int], L: int, R: int) -> int:
      if L == R:
        return nums[L]
      middle = (R + L) // 2
      if nums[middle-1] == nums[middle]:
        len_l = middle-1 - L
        if len_l % 2 == 1:
          return binarySearch(nums, L, middle-2) # go left
        else:
          return binarySearch(nums, middle+1, R) # go right
      elif nums[middle+1] == nums[middle]:
        len_r = R - middle+1
        if len_r % 2 == 1:
          return binarySearch(nums, middle+2, R)
        else:
          return binarySearch(nums, L, middle-1)
      else:
        return nums[middle] # middle is single element

    return binarySearch(nums, 0, len(nums)-1)
