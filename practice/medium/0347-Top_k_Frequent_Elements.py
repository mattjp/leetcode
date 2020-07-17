class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = collections.Counter(nums)
    k_most_common = counter.most_common(k)
    return list(map(lambda x: x[0], k_most_common))
