class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums = nums1[:m]
    i = j = k = 0
    while i < m or j < n:
      x = nums[i] if i < m else 1000 # placeholder
      y = nums2[j] if j < n else 1000
      if x <= y:
        nums1[k] = x
        i += 1
      else:
        nums1[k] = y
        j += 1
      k += 1
