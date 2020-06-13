class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    """
    keep all subsets sorted by length
    once a number can be added to a subset, add it then stop iterating
    """

    if len(nums) < 1:
      return []

    sorted_nums = sorted(nums)
    subsets = []

    for num in sorted_nums:          
      for subset in subsets:
        if num % subset[-1] == 0:
          subset_copy = subset.copy() # copy so we don't overwrite the original set
          subset_copy.append(num)
          subsets.append(subset_copy)
          break
      else:
        subsets.append([num]) # create a new subset if no other subsets contain a divisor for `num`
      subsets.sort(key=lambda s: len(s), reverse=True) # keep longest subsets in front

    return subsets[0]
