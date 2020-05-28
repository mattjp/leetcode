class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # iterating from right to left, find first decreasing element index `a`
    i = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
      i -= 1
    a = i-1

    # iterating from left to right (starting at `i`), find the element that 
    # is the smallest element that is larger than the element at index `a`
    while i <= len(nums)-2 and nums[i+1] > nums[a]:
      i += 1

    # swap elements at index `i` and `a`
    # this puts the next largest element at index `a`, one step closer to strictly increasing
    tmp = nums[i]
    nums[i] = nums[a]
    nums[a] = tmp

    # since we're looking for the next largest permutation, we know the smallest permutation
    # will be the sorted array, so we sort all elements after index `a`
    nums[a+1:] = sorted(nums[a+1:])                
