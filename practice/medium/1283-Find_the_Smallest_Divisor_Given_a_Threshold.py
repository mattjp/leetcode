class Solution:
  def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    """
    disguised binary search
    """

    def divideAndSum(n: List[int], d: int) -> int:
      """
      divide all numbers in n by d, rounding up
      return the sum of these new numbers
      """
      return sum(map(lambda x: math.ceil(x/d), n))

    d_max = max(nums)
    d_min = 1

    while d_max != d_min:
      m = (d_max + d_min) // 2
      s = divideAndSum(nums, m)
      if s > threshold:
        d_min = m+1 # +1 because otherwise `max` and `min` will never run into each other
      elif s <= threshold: # lteq because we want the _smallest_ divisor, not the first that matches
        d_max = m
    return d_max
