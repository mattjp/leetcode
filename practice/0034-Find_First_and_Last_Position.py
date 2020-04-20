class Solution:
  def binarySearch(self, nums: List[int], t: int, l: int, r: int) -> int:
    n = (l + r) // 2
    if nums[n] == t:
      return n
    if l == r or n < 0 or n > len(nums)-1:
      return -1
    if nums[n] < t:
      return self.binarySearch(nums, t, n+1, r)
    if nums[n] > t:
      return self.binarySearch(nums, t, l, n-1)

  def expand(self, nums: List[int], target: int, n: int) -> List[int]:
    l, r = n, n
    while r < len(nums)-1 and nums[r+1] == target:
      r += 1
    while l > 0 and nums[l-1] == target:
      l -= 1
    return [l, r]

  def searchRange(self, nums: List[int], target: int) -> List[int]:
    if len(nums) < 1:
      return [-1, -1]
    ns = self.binarySearch(nums, target, 0, len(nums)-1)
    if ns == -1:
      return [-1, -1]
    return self.expand(nums, target, ns)
