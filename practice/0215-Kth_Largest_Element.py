# 215. Kth Largest Element in an Array
#
# Find the kth largest element in an unsorted array. Note that it is the kth 
# largest element in the sorted order, not the kth distinct element.

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    nums_sorted = sorted(nums)
    nums_sorted.reverse()
    return nums_sorted[k-1]
