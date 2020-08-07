class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    counter = collections.Counter(nums)
    output = list(filter(lambda x: x[1] > 1, counter.items()))
    return list(map(lambda x: x[0], output))
