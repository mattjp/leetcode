# note: problem asked to be solved in O(n) time
# solved using O(n) extra memory
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    counter = collections.Counter(nums)
    return counter.most_common()[-1][0]
