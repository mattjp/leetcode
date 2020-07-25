class Solution:
  def findMin(self, nums: List[int]) -> int:
    # return min(nums) # this actually worked lol

    def bs(l: int, r: int, nums: List[int]):
        m = (l + r) // 2
        if (
          m == 0
          or m == len(nums)-1
          or l == r
          or nums[m] < nums[m-1]
        ):
          return nums[m]
        if (nums[m+1] < nums[m]):
          return nums[m+1]

        # go right if all numbers to the left are monotonically increasing
        if nums[l] < nums[m] and nums[r-1] < nums[l]:
          return bs(m+1, r, nums)
        # go left
        else:
          return bs(l, m, nums)

    nums = sorted(list(set(nums))) # remove dupes inefficently, can do linearly
    return bs(0, len(nums), nums) if len(nums) > 3 else min(nums) # lazy error checking lol
