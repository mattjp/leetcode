class Solution:
  def search(self, nums: List[int], target: int) -> int:

    def findPivot(nums: List[int]) -> int:
      i = 1
      while i < len(nums) and nums[i] > nums[i-1]:
        i += 1
      return i

    def binarySearch(nums: List[int], l: int, r: int, target: int) -> int:
      m = (l + r ) // 2
      if l == m or r == m:
        return m if nums[m] == target else -1
      if nums[m] == target:
        return m
      if nums[m] < target:
        return binarySearch(nums, m, r, target)
      if nums[m] > target:
        return binarySearch(nums, l, m, target)

    if len(nums) < 1:
      return -1
    pivot = findPivot(nums)
    sorted_nums = nums[pivot:] + nums[:pivot]
    index = binarySearch(sorted_nums, 0, len(sorted_nums), target)
    if index == -1:
      return -1
    else:
      return (index + pivot) % len(nums)
