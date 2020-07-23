class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    output = []
    counter = collections.Counter(nums)
    for k,v in counter.items():
      if v == 1:
        output.append(k)

    return output
